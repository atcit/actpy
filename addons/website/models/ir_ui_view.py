# -*- coding: ascii -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

import logging
from itertools import groupby

from actpy import api, fields, models, _
from actpy import tools
from actpy.addons.http_routing.models.ir_http import url_for
from actpy.http import request
from actpy.tools import pycompat

_logger = logging.getLogger(__name__)


class View(models.Model):

    _name = "ir.ui.view"
    _inherit = ["ir.ui.view", "website.seo.metadata"]

    customize_show = fields.Boolean("Show As Optional Inherit", default=False)
    # @todo actpy:
    # Remove ondelete='cascade' (But need to check side-effects!!)
    #
    # When we Uninstall ``website`` module then some of
    # ``portal`` module views are also deleted (For Ex. portal_show_sign_in)
    # Find proper way to do the same, remove website_id from different
    # module's view & keep those views, do not delete those views permanently.
    website_id = fields.Many2one('website', ondelete='cascade', string="Website")
    page_ids = fields.One2many('website.page', compute='_compute_page_ids', store=False)
    is_cloned = fields.Boolean(string='Cloned', copy=False, default=False,
                               help="This view is cloned"
                                    "(not present physically in file system) "
                                    "from default website's view for "
                                    "supporting multi-website feature.")

    @api.one
    def _compute_page_ids(self):
        self.page_ids = self.env['website.page'].search(
            [('view_id', '=', self.id)]
        )

    @api.multi
    def unlink(self):
        result = super(View, self).unlink()
        self.clear_caches()
        return result

    @api.multi
    def _sort_suitability_key(self):
        """ Key function to sort views by descending suitability
            Suitability of a view is defined as follow:
                * if the view and request website_id are matched
                * then if the view has no set website
        """
        self.ensure_one()
        context_website_id = self.env.context.get('website_id', 1)
        website_id = self.website_id.id or 0
        different_website = context_website_id != website_id
        return (different_website, website_id)

    def filter_duplicate(self):
        """ Filter current recordset only keeping the most suitable view per distinct key """
        filtered = self.env['ir.ui.view']
        for dummy, group in groupby(self, key=lambda record: record.key):
            filtered += sorted(group, key=lambda record: record._sort_suitability_key())[0]
        return filtered

    @api.model
    def _view_obj(self, view_id):
        if isinstance(view_id, pycompat.string_types):
            if 'website_id' in self._context:
                domain = [('key', '=', view_id), '|', ('website_id', '=', False), ('website_id', '=', self._context.get('website_id'))]
                order = 'website_id'
            else:
                domain = [('key', '=', view_id)]
                order = self._order
            views = self.search(domain, order=order)
            if views:
                return views.filter_duplicate()
            else:
                return self.env.ref(view_id)
        elif isinstance(view_id, pycompat.integer_types):
            return self.browse(view_id)

        # assume it's already a view object (WTF?)
        return view_id

    @api.model
    def _get_inheriting_views_arch_domain(self, view_id, model):
        domain = super(View, self)._get_inheriting_views_arch_domain(view_id, model)
        return ['|', ('website_id', '=', False), ('website_id', '=', self.env.context.get('website_id'))] + domain

    @api.model
    @tools.ormcache_context('self._uid', 'xml_id', keys=('website_id',))
    def get_view_id(self, xml_id):
        if 'website_id' in self._context and not isinstance(xml_id, pycompat.integer_types):
            domain = [('key', '=', xml_id), '|', ('website_id', '=', self._context['website_id']), ('website_id', '=', False)]
            view = self.search(domain, order='website_id', limit=1)
            if not view:
                _logger.warning("Could not find view object with xml_id '%s'", xml_id)
                raise ValueError('View %r in website %r not found' % (xml_id, self._context['website_id']))
            return view.id
        return super(View, self).get_view_id(xml_id)

    @api.multi
    def render(self, values=None, engine='ir.qweb'):
        """ Render the template. If website is enabled on request, then extend rendering context with website values. """
        new_context = dict(self._context)
        if request and getattr(request, 'is_frontend', False):

            editable = request.website.is_publisher()
            translatable = editable and self._context.get('lang') != request.website.default_lang_code
            editable = not translatable and editable

            # in edit mode ir.ui.view will tag nodes
            if not translatable and not self.env.context.get('rendering_bundle'):
                if editable:
                    new_context = dict(self._context, inherit_branding=True)
                elif request.env.user.has_group('website.group_website_publisher'):
                    new_context = dict(self._context, inherit_branding_auto=True)

        if self._context != new_context:
            self = self.with_context(new_context)
        return super(View, self).render(values, engine=engine)

    @api.model
    def _prepare_qcontext(self):
        """ Returns the qcontext : rendering context with website specific value (required
            to render website layout template)
        """
        qcontext = super(View, self)._prepare_qcontext()

        if request and getattr(request, 'is_frontend', False):
            editable = request.website.is_publisher()
            translatable = editable and self._context.get('lang') != request.env['ir.http']._get_default_lang().code
            editable = not translatable and editable

            if 'main_object' not in qcontext:
                qcontext['main_object'] = self

            qcontext.update(dict(
                self._context.copy(),
                website=request.website,
                url_for=url_for,
                res_company=request.website.company_id.sudo(),
                default_lang_code=request.env['ir.http']._get_default_lang().code,
                languages=request.env['ir.http']._get_language_codes(),
                translatable=translatable,
                editable=editable,
                menu_data=self.env['ir.ui.menu'].load_menus_root() if request.website.is_user() else None,
            ))

        return qcontext

    @api.model
    def get_default_lang_code(self):
        website_id = self.env.context.get('website_id')
        if website_id:
            lang_code = self.env['website'].browse(website_id).default_lang_code
            return lang_code
        else:
            return super(View, self).get_default_lang_code()

    @api.multi
    def redirect_to_page_manager(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/website/pages',
            'target': 'self',
        }

    # Multi Website: Automated Action On Create Rule
    ##################################################
    # If views are manually created for default website,
    # then it'll automatically cloned for other websites.
    #
    # As this method is also called when new website is created.
    # Because at the time of website creation ``Home`` page will be cloned,
    # So, this method will automatically triggered to
    # cloned all customize view(s).
    @api.model
    def multi_website_view_rule(self):
        default_website = self.env['website'].search([
            ('is_default_website', '=', True)])
        ir_model_data = self.env['ir.model.data']
        for website in self.env['website'].search(
                [('is_default_website', '=', False)]):
            for cus_view in self.search(
                    [('website_id', '=', default_website.id),
                     ('customize_show', '=', True),
                     ('is_cloned', '=', False),
                     '|', ('active', '=', False), ('active', '=', True)]):
                if not self.search(
                        [('key', '=', cus_view.key +
                            '_' + website.website_code),
                         '|', ('active', '=', False), ('active', '=', True)]):
                    new_cus_view = cus_view.copy(
                        {'is_cloned': True,
                         'key': cus_view.key + '_' + website.website_code,
                         'website_id': website.id
                         })
                    new_inherit_id = self.search(
                        [('key', '=', new_cus_view.inherit_id.key +
                         '_' + website.website_code),
                         '|', ('active', '=', False), ('active', '=', True)])
                    if new_cus_view.inherit_id and new_inherit_id:
                        new_cus_view.write({
                            'inherit_id': new_inherit_id.id,
                        })
                    model_data_id = ir_model_data.create({
                        'model': cus_view.model_data_id.model,
                        'name': cus_view.model_data_id.name +
                        '_' + website.website_code,
                        'res_id': new_cus_view.id,
                        'module': cus_view.model_data_id.module,
                    })
                    new_cus_view.write({
                        'model_data_id': model_data_id
                    })

    # Add the website_id to each customize QWeb view(s) at the time
    # of creation of new customize QWeb view(s).
    @api.model
    def create(self, values):
        # For Theme's View(s)
        if values.get('key') and values.get('type') == 'qweb' and \
                self.env.context.get('install_mode_data'):
            module_name = self.env.context['install_mode_data']['module']
            module_obj = self.env['ir.module.module'].sudo().search(
                [('name', '=', module_name)])
            if module_obj and \
                    (module_obj.category_id.name == 'Theme'
                     or (module_obj.category_id.parent_id
                         and module_obj.category_id.parent_id.name
                         == 'Theme')):
                values.update({
                    'website_id': module_obj.website_ids.id,
                })
        return super(View, self).create(self._compute_defaults(values))

    # Keep other website's view as it is when run server using -i/-u
    # As other website's views are not present anywhere in FS(file system).
    # So, once those are created/cloned from default website,
    # they can be changed/updated via debug mode only(ir.ui.view)
    # Menu: Settings/Technical/User Interface/Views
    #
    # Scenario 1:
    # -----------
    # For Delete those views, Manually set ``is_cloned`` field to ``False``
    # @todo actpy:
    # But Actually View is not deleted, It'll create again from
    # default website's view,
    # Find a way to delete website specific views form DB.
    #
    # Scenario 2:
    # -----------
    # If you write the code for already cloned views in FS(file system)/Module
    # to upgrade/update those views, then at the time of module update
    # process that cloned views id are found in FS(file system)/Module,
    # So in those particular views ``is_cloned`` will automatically
    # set to ``False`` (Definitely it'll be done from another method!!),
    # because now those views are not anymore cloned,
    # now they are physically present!!
    @api.multi
    def unlink(self):
        for view in self:
            if view.is_cloned:
                # Do not delete cloned view(s)
                # ----------------
                # 'View(s) that you want delete are '
                # 'cloned view(s).\n'
                # 'Cloned view(s) are automatically created '
                # 'for supporting multi website feature.\n'
                # 'If you still want to delete this view(s) '
                # 'then first Uncheck(set to False) the '
                # 'cloned field.\n'
                # 'By deleting cloned view(s) multi website '
                # 'will not work properly.\n'
                # 'So, Be sure before deleting view(s).'
                return True
            return super(View, view).unlink()

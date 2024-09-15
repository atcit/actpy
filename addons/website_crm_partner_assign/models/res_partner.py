# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import api, fields, models
from actpy.addons.http_routing.models.ir_http import slug


class ResPartnerGrade(models.Model):
    _name = 'res.partner.grade'
    _inherit = ['website.published.mixin']

    def _default_website(self):
        default_website_id = self.env.ref('website.default_website')
        return [default_website_id.id] if default_website_id else None

    website_published = fields.Boolean(default=True)
    sequence = fields.Integer('Sequence')
    active = fields.Boolean('Active', default=lambda *args: 1)
    name = fields.Char('Level Name', translate=True)
    partner_weight = fields.Integer('Level Weight', default=1,
        help="Gives the probability to assign a lead to this partner. (0 means no assignation.)")
    website_ids = fields.Many2many('website', 'website_partner_grade_pub_rel',
                                   'website_id', 'partner_grade_id',
                                   string='Websites', copy=False,
                                   default=_default_website,
                                   help='List of websites in which '
                                        'Partner Grade will published.')

    @api.multi
    def _compute_website_url(self):
        super(ResPartnerGrade, self)._compute_website_url()
        for grade in self:
            grade.website_url = "/partners/grade/%s" % (slug(grade))


class ResPartnerActivation(models.Model):
    _name = 'res.partner.activation'
    _order = 'sequence'

    sequence = fields.Integer('Sequence')
    name = fields.Char('Name', required=True)


class ResPartner(models.Model):
    _inherit = "res.partner"

    partner_weight = fields.Integer('Level Weight', default=lambda *args: 0,
        help="Gives the probability to assign a lead to this partner. (0 means no assignation.)")
    grade_id = fields.Many2one('res.partner.grade', 'Level')
    grade_sequence = fields.Integer(related='grade_id.sequence', readonly=True, store=True)
    activation = fields.Many2one('res.partner.activation', 'Activation', index=True)
    date_partnership = fields.Date('Partnership Date')
    date_review = fields.Date('Latest Partner Review')
    date_review_next = fields.Date('Next Partner Review')
    # customer implementation
    assigned_partner_id = fields.Many2one(
        'res.partner', 'Implemented by',
    )
    implemented_partner_ids = fields.One2many(
        'res.partner', 'assigned_partner_id',
        string='Implementation References',
    )
    implemented_count = fields.Integer(compute='_compute_implemented_partner_count', store=True)

    @api.one
    @api.depends('implemented_partner_ids', 'implemented_partner_ids.website_published', 'implemented_partner_ids.active')
    def _compute_implemented_partner_count(self):
        self.implemented_count = len(self.implemented_partner_ids.filtered('website_published'))

    @api.onchange('grade_id')
    def _onchange_grade_id(self):
        grade = self.grade_id
        self.partner_weight = grade.partner_weight if grade else 0

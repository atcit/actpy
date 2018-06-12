# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

import actpy.exceptions
import actpy.osv.osv
from actpy import models, api
from actpy.tools.safe_eval import safe_eval

class m(models.Model):
    """ This model exposes a few methods that will raise the different
        exceptions that must be handled by the server (and its RPC layer)
        and the clients.
    """
    _name = 'test.exceptions.model'

    @api.multi
    def generate_except_osv(self):
        # title is ignored in the new (6.1) exceptions
        raise actpy.osv.osv.except_osv('title', 'description')

    @api.multi
    def generate_except_orm(self):
        # title is ignored in the new (6.1) exceptions
        raise actpy.exceptions.except_orm('title', 'description')

    @api.multi
    def generate_warning(self):
        raise actpy.exceptions.Warning('description')

    @api.multi
    def generate_redirect_warning(self):
        action = self.env.ref('test_exceptions.action_test_exceptions')
        raise actpy.exceptions.RedirectWarning('description', action.id, 'Go to the redirection')

    @api.multi
    def generate_access_denied(self):
        raise actpy.exceptions.AccessDenied()

    @api.multi
    def generate_access_error(self):
        raise actpy.exceptions.AccessError('description')

    @api.multi
    def generate_exc_access_denied(self):
        raise Exception('AccessDenied')

    @api.multi
    def generate_undefined(self):
        self.surely_undefined_symbol

    @api.multi
    def generate_user_error(self):
        raise actpy.exceptions.UserError('description')

    @api.multi
    def generate_missing_error(self):
        raise actpy.exceptions.MissingError('description')

    @api.multi
    def generate_validation_error(self):
        raise actpy.exceptions.ValidationError('description')

    @api.multi
    def generate_except_osv_safe_eval(self):
        self.generate_safe_eval(self.generate_except_osv)

    @api.multi
    def generate_except_orm_safe_eval(self):
        self.generate_safe_eval(self.generate_except_orm)

    @api.multi
    def generate_warning_safe_eval(self):
        self.generate_safe_eval(self.generate_warning)

    @api.multi
    def generate_redirect_warning_safe_eval(self):
        self.generate_safe_eval(self.generate_redirect_warning)

    @api.multi
    def generate_access_denied_safe_eval(self):
        self.generate_safe_eval(self.generate_access_denied)

    @api.multi
    def generate_access_error_safe_eval(self):
        self.generate_safe_eval(self.generate_access_error)

    @api.multi
    def generate_exc_access_denied_safe_eval(self):
        self.generate_safe_eval(self.generate_exc_access_denied)

    @api.multi
    def generate_undefined_safe_eval(self):
        self.generate_safe_eval(self.generate_undefined)

    @api.multi
    def generate_user_error_safe_eval(self):
        self.generate_safe_eval(self.generate_user_error)

    @api.multi
    def generate_missing_error_safe_eval(self):
        self.generate_safe_eval(self.generate_missing_error)

    @api.multi
    def generate_validation_error_safe_eval(self):
        self.generate_safe_eval(self.generate_validation_error)

    @api.multi
    def generate_safe_eval(self, f):
        globals_dict = { 'generate': f }
        safe_eval("generate()", mode='exec', globals_dict=globals_dict)

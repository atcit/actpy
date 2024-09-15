# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

from actpy import api, fields, models


class MailMail(models.Model):

    _inherit = "mail.mail"

    fetchmail_server_id = fields.Many2one('fetchmail.server', "Inbound Mail Server", readonly=True, index=True, oldname='server_id')

    @api.model
    def create(self, values):
        fetchmail_server_id = self.env.context.get('fetchmail_server_id')
        if fetchmail_server_id:
            values['fetchmail_server_id'] = fetchmail_server_id
        return super(MailMail, self).create(values)

    @api.multi
    def write(self, values):
        fetchmail_server_id = self.env.context.get('fetchmail_server_id')
        if fetchmail_server_id:
            values['fetchmail_server_id'] = fetchmail_server_id
        return super(MailMail, self).write(values)

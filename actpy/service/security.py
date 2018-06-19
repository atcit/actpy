# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

import actpy
import actpy.exceptions

def login(db, login, password):
    res_users = actpy.registry(db)['res.users']
    return res_users._login(db, login, password)

def check(db, uid, passwd):
    res_users = actpy.registry(db)['res.users']
    return res_users.check(db, uid, passwd)

def compute_session_token(session):
    with actpy.registry(session.db).cursor() as cr:
        self = actpy.api.Environment(cr, session.uid, {})['res.users'].browse(session.uid)
        return self._compute_session_token(session.sid)

def check_session(session):
    with actpy.registry(session.db).cursor() as cr:
        self = actpy.api.Environment(cr, session.uid, {})['res.users'].browse(session.uid)
        if actpy.tools.misc.consteq(self._compute_session_token(session.sid), session.session_token):
            return True
        self._invalidate_session_cache()
        return False

actpy.define('iap.redirect_actpy_credit_widget', function(require) {
"use strict";

var core = require('web.core');
var framework = require('web.framework');
var Widget = require('web.Widget');
var QWeb = core.qweb;


var IapactpyCreditRedirect = Widget.extend({
    template: 'iap.redirect_to_actpy_credit',
    events : {
        "click .redirect_confirm" : "actpy_redirect",
    },
    init: function (parent, action) {
        this._super(parent, action);
        this.url = action.params.url;
    },

    actpy_redirect: function () {
        window.open(this.url, '_blank');
        this.do_action({type: 'ir.actions.act_window_close'});
        // framework.redirect(this.url);
    },

});
core.action_registry.add('iap_actpy_credit_redirect', IapactpyCreditRedirect);
});

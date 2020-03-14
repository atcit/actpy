actpy.define('web.GanttView', function (require) {
"use strict";

var AbstractView = require('web.AbstractView');
var core = require('web.core');
var GanttModel = require('web.GanttModel');
var GanttRenderer = require('web.GanttRenderer');
var Controller = require('web.GanttController');

var _lt = core._lt;

var GanttView = AbstractView.extend({
    display_name: _lt('Gantt'),
    icon: 'fa-tasks',
    config: {
        Model: GanttModel,
        Controller: Controller,
        Renderer: GanttRenderer,
    },
    /**
     * @override
     */
    init: function(viewInfo) {
        this._super.apply(this, arguments);
        var arch = viewInfo.arch;
        this.loadParams.arch = arch;
    },
});

return GanttView;

});

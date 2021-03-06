/**
 * Created by Administrator on 12/05/2016.
 */
define(function (require) {
    "use strict";
    var _ = require("underscore"),
        Backbone = require('backbone'),
        Recipe = require('models/RecipeModel'),
        Cookbook = require('models/CookbookModel');

    return Backbone.View.extend({
        model: Recipe,

        initialize: function () {
            this.template = _.template('<option value="<%=id%>"><%= name %></option>');
            this.render();
        },

        render: function () {
            this.setElement(this.template(this.model.attributes));
            return this;
        }
    })
});
/**
 * Created by Administrator on 12/05/2016.
 */
var cb1 = new CookBook({ id: 1, name: "CookBook 1" });
var cb2 = new CookBook({ id: 2, name: "CookBook 2" });

var cbCol = new CookBooks([cb1,cb2]);
var cbookList = null;

$(document).ready(function () {
    cbookList = new CookBooksView({ el: 'body', model: cbCol });
    cbookList.render();
});
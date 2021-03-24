var navigation = {"links":
    [
        {
            "url":"index.html",
            "name":"About"
        },
        {
            "url":"https://www.notion.so/rshaw/School-Notes-882d824f9d3b4d30945a25c5b2dbdc1e",
            "name":"Notes"
        },
        {
            "url":"photo.html",
            "name":"Photos"
        },
        {
            "url":"othersites.html",
            name:"On Other Sites"
        }
]};

var template = Handlebars.compile($("#nav-elements").html());

var genhtml = template(navigation);

$("#topnav").html(genhtml);
$("#sidenav").html(genhtml);

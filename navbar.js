var navigation = {"links":
    [
        {
            "url":"index.html",
            "name":"About"
        },
        {
            "url":"https://rshaw.notion.site/subject-notes?pvs=4",
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

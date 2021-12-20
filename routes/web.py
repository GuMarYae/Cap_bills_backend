"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "BillController@index").name("index"),
        Get("/@id", "BillController@show").name("show"),
        Post("/", "BillController@create").name("create"),
        Put("/@id", "BillController@update").name("update"),
        Delete("/@id", "BillController@destroy").name("destroy")
    ], prefix="/bills", name="bills")
]


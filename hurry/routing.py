import re

class Router(object):
    routes = ()

    def __init__(self, routes=None):
        self.routes = routes

    def add_route(self, url, method, handler):
        self.routes += (
            Route(url, method, handler),
        )
        print(self.routes)

    def find_route(self, method, url):
        for route in self.routes:
            if(route.method == method and route.url == url):
                return route
        return None

class Route(object):
    def __init__(self, url, method, handler):
        self.url = url
        self.method = method
        self.handler = handler

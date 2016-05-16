class Router(object):
"""

"""
    routes = {}

    def __init__(self, routes=None):
        if isinstance(routes, dict):
            for route in routes:
                self.add_route(route)

    def add_route(self, route):
        self.routes[url] = handler

    def find_route(self, path):
        for route in self.routes:
            match = re.search(route.regex_pattern, path)
            if match:
                return route
        return None


class Route(object):
    def __init__(self, url, method, handler)
        self.url = url
        self.handler = handler
        self.regex_pattern = self.generate_regex_pattern()

from webob                 import Request, Response
from wsgiref.simple_server import make_server
from hurry.routing         import Router
from hurry.http            import Response, Request
import json

class Hurry(object):
    def __init__(self, routes=()):
        self.router = Router(routes)

    def __call__(self, environ, start_response):
        self.request = Request(environ)
        self.response = Response()
        path = self.request.path_info
        method = self.request.method
        route = self.router.find_route(method, path)
        if(route):
            route.handler(self.request, self.response)
        return self.response(environ, start_response)

    def run(self, host=None, port=None):
        host = '127.0.0.1'
        port = 9000
        server = make_server(host, port, self)
        server.serve_forever()

    def get(self,url):
        def decorator(f):
            self.router.add_route(url, 'GET', f)
        return decorator

    def post(self,url):
        def decorator(f):
            self.router.add_route(url, 'POST', f)
        return decorator

    def put(self,url):
        def decorator(f):
            self.router.add_route(url, 'PUT', f)
        return decorator

    def delete(self,url):
        def decorator(f):
            self.router.add_route(url, 'DELETE', f)
        return decorator

class Route(object):
    def __init__(self, url, method, handler):
        self.url = url
        self.method = method
        self.handler = handler

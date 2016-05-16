from webob import Request, Response
from wsgiref.simple_server import make_server

class Hurry(object):
    def __init__(self, routes=None):
        self.routes = routes

    def __call__(self, environ, start_response):
        req = Request(environ)
        res = Response()
        res.write('Hello World')
        return res(environ, start_response)

    def run(self, host=None, port=None):
        host = '127.0.0.1'
        port = 9000
        server = make_server(host, port, self)
        server.serve_forever()

    def static(self, url=None, path=None):
        Static.serve(url, path)

    def get(self, url, handler):
        Router.add_route(url, 'GET', handler)

    def post(self, url, handler):
        Router.add_route(url, 'POST', handler)

    def put(self, url, handler):
        Router.add_route(url, 'PUT', handler)

    def delete(self, url, handler):
        Router.add_route(url, 'DELETE', handler)

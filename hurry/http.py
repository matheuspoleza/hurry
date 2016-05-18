# -*- coding: utf-8 -*-
from webob import Request as WebObRequest, Response as WebObResponse

Request = WebObRequest
Response = WebObResponse

class RequestHandler():
    def __init__(self, response):
        self.response = response

    def render(self, template, engine):
        self.response.write(template)

    def status(self, status, data):
        self.response.write('error')
        self.response.status = status

    def send(self, res):
        self.response.write(res)

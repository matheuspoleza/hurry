# -*- coding: utf-8 -*-
from hurry.app import Hurry

app = Hurry()

@app.get('/api')
def hello_world(req, res):
    res.send('hello, world!')

@app.get('/api/error')
def hello(req, res):
    res.status(404, { 'error': 'Message is required '})

if __name__ == '__main__':
    app.run()

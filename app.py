from hurry.app import Hurry

app = Hurry()

@app.get('/hello')
def hello_world(req, res):
    print('hello, world!')

@app.post('/hello')
def save_hello(req, res):
    print('new hello saved!')

if __name__ == '__main__':
    app.run()

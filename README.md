# hurry
> A flexible and quickly Python Micro Web Framework

### Status
Work in progress

### What is different?
- Request and response manipulation
- Flexible template engine, with many supports
- Asynchronous requests support 

### Getting started

```sh
pip install hurry
```

```python
from hurry.app import Hurry

app = Hurry()

@app.get('/hello')
def hello(req, res):
  res.send('hello, world!')
  
if __name__ == '__main__':
  app.run()
```

## License
MIT

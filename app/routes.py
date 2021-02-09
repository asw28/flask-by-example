from app import app

@app.route('/')
def hello():
    return "Root of flask-by-example"
    

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()

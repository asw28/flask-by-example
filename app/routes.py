from app import app

@app.route('/')
def hello():
    return "Root of flask-by-example"
    

@app.route('/<name>')
def index():
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

if __name__ == '__main__':
    app.run()

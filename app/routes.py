from app import app

@app.route('/')
def hello():
    return "Root of flask-by-example"
    

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Knobber'}
    return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
    app.run()

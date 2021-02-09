from app import app

from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Knobber'}
    reports = {'report1': 'slug1',
               'report2': 'slug2'}
    return render_template('index.html', title='index', user=user, reports=reports)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
    
@app.route('/slug1')
def slug1():
    user = {'username': 'Knobber'}
    info = {'pagetitle': 'report1'}
    return render_template('report.html', title=info['pagetitle'], info=info, user=user)

@app.route('/slug2')
def slug2():
    user = {'username': 'Knobber'}
    info = {'pagetitle': 'report2'}
    return render_template('report.html', title=info['pagetitle'], info=info, user=user)    


if __name__ == '__main__':
    app.run()

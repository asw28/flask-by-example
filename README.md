## running flask app on heroku

From here: https://realpython.com/flask-by-example-part-1-project-setup/


### u wot m8

heroku create wordcount-pro-1337

git remote add pro git@heroku.com:wordcount-pro-1337.git

heroku create wordcount-stage-1337

git remote add stage git@heroku.com:wordcount-stage-1337.git


### setting configs

heroku config:set APP_SETTINGS=config.StagingConfig --remote stage

heroku config:set APP_SETTINGS=config.ProductionConfig --remote pro


### running locally from remote app

heroku run python app.py --app wordcount-pro-1337

heroku run python app.py --app wordcount-stage-1337



### alembic stuff

python manage.py db init

python manage.py db migrate

python manage.py db upgrade

### notes


<html>
    <head>
        <title>{{ title }} - Microblog</title>
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
</html>


<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Report Directory</title>
    </head> 
    <body>
        <ul>
        {% for r in reports %}
            <li>
                <a href="{{ url_for('page', slug=r) }}">{{ r }}</a>
            </li>
        {% endfor %}
        </ul>
    </body>
</html> 
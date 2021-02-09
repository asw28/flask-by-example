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
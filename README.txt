NewBrain is a system for getting you own back on annoying people that cold call you or attempt to hack you.
It provides an automated reverse DOS attack on them to stop them and let them know who's boss.

Currently it's WIP but once deployed it will help keep you safe.

Any contributions are more than welcome.

More to come soon.

INSTALLATION INSTRUCTIONS
=========================

You need
Python 2.7+
Pip
Download the repository from https://github.com/muce/newbrain
Then, pip install -r requirements.txt

CELERY
======

Create a virtualenv and install the requirements. virtualenv venv
Open a second terminal window and start a local Redis server (if you are on Linux or Mac, execute run-redis.sh to install and launch a private copy).
Open a third terminal window. Set two environment variables MAIL_USERNAME and MAIL_PASSWORD to a valid Gmail account credentials (these will be used to send test emails). Then start a Celery worker: venv/bin/celery worker -A app.celery --loglevel=info.


OPERATION
=========

source venv/bin/activate
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py runserver
Go to http://localhost:5000/ and enjoy this application!


Many thanks to Miguel Grinberg for his expert help.

Thanks all you nice people X

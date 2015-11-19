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


OPERATION
=========

pip install -r requirements.txt
virtualenv venv
source venv/bin/activate
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
./run-redis.sh
Set two environment variables MAIL_USERNAME and MAIL_PASSWORD to a valid Gmail account credentials (these will be used to send test emails).
venv/bin/celery worker -A app.celery --loglevel=info.
python manage.py runserver
Go to http://localhost:5000/ and enjoy this application!


Many thanks to Miguel Grinberg for his expert help.

Thanks all you nice people X

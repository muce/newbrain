from flask import flash

from app.main.models import *
from errors import *
from forms import *
from models import *
import os
import random
import time
from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify
from flask.ext.mail import Mail, Message
from celery import Celery


# Celery configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

app = Flask(__name__)
conf = app.config

# Initialize extensions
#mail = Mail(app)

# Initialize Celery
#celery = Celery(app.name, broker=CELERY_BROKER_URL
#celery.conf.update(app.config)


@main.route('/')
def index():
    current_user = User()
    print current_user
    return render_template('index.html',
                            user = 'user',
                            current_user = current_user,
                            main_menu_url = 'http://localhost:5000/menu')


@main.route('/targets', methods=['GET', 'POST'])
def targets():
    app = current_app._get_current_object()
    phone = None
    email = None
    website = None
    form = TargetForm()
    if form.validate_on_submit():
        phone = form.phone.data
        email = form.email.data
        website = form.website.data
        new_one = Target.query.filter_by(phone=phone).first()
        if new_one is None:
            target = Target(phone=phone, email=email, website=website)
            db.session.add(target)
            flash("Added Target: "+str(phone)+", "+str(email)+", "+str(website))
        else:
            flash("Didn't add Target: "+str(phone)+", "+str(email)+", "+str(website))
        form.phone.data = ''
        form.email.data = ''
        form.website.data = ''
    return render_template('/targets.html',
                            user = 'user',
                            form = form,
                            targets = Target.query.all(),
                            phone = phone,
                            email = email,
                            website = website)

"""
@celery.task
def send_async_email(msg):
    #Background task to send an email with Flask-Mail.
    # Initialize extensions
    app = current_app._get_current_object()
    conf = app.config
    mail = Mail(app)
    print 'conf: '+conf
    print 'mail: '+mail
    # Initialize Celery
    #celery = Celery(app.name, broker=conf['CELERY_BROKER_URL'])
    #celery.conf.update(app.config)

    with app.app_context():
        mail.send(msg)


@celery.task(bind=True)
def long_task(self):
    #Background task that runs a long function with progress reports.
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}
"""


@main.route('/send_email', methods=['GET', 'POST'])
def send_email():
    """
    if request.method == 'GET':
        return render_template('/send_index.html', email=session.get('email', ''))
    email = request.form['email']
    session['email'] = email

    # send the email
    msg = Message('Hello from NewBrain. This is just a warning',
                  recipients=[request.form['email']])
    msg.body = "Sousou is the boss, OK?"
    if request.form['submit'] == 'Send':
        # send right away
        send_async_email.delay(msg)
        flash('Sending email to {0}'.format(email))
    else:
        # send in one minute
        send_async_email.apply_async(args=[msg], countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))
    """
    form = EmailForm()
    return render_template('/send_email.html',
                           form = form)
"""

@main.route('/longtask', methods=['POST'])
def longtask():
    task = long_task.apply_async()
    return jsonify({}), 202, {'Location': url_for('taskstatus',
                                                  task_id=task.id)}


@main.route('/status/<task_id>')
def taskstatus(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)
"""


"""
@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)
"""
from flask import flash

from app.main.models import *
from errors import *
from forms import *
from models import *


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
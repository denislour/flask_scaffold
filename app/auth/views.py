from flask import Blueprint, request, render_template, \
    flash, session, redirect, url_for
from werkzeug.security import check_password_hash
from .forms import LoginForm
from .models import User

auth = Blueprint(
    'auth', __name__,
    template_folder="templates",
)


@auth.route('/login/', methods=['GET', 'POST'])
def login():

    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('auth.home'))
        flash('Wrong email or password', 'error-message')

    return render_template("auth.j2", form=form)

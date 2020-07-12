from flask import Blueprint, request, render_template, \
    flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app import db
from .forms import LoginForm, RegistrationForm
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
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('core.index')
            return redirect(next)
        flash('Invalid username or password')

    return render_template("login.jinja2", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('core.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        flash("You can login now.")
        return redirect(url_for('auth.login'))
    return render_template('register.jinja2', form=form)

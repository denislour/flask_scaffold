from flask import Blueprint, request, render_template, \
    flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.core.email import send_email
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
        token = user.generate_confirmation_token()
        send_email(
            current_user.email, 'Confirm your account',
            'emails/confirm.jinja2', user=current_user, token=token,
        )
        flash("You can login now.")
        return redirect(url_for('auth.login'))
    return render_template('register.jinja2', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirm:
        return redirect(url_for('core.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed your account. Thanks!')
    else:
        flash('Confirm link is invalid or expired')
    return redirect(url_for('core.index'))


@auth.before_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.blueprint != 'auth' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('core.index'))
    return render_template('unconfirmed.jinja2')


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    print(current_user.email)
    send_email(
        current_user.email, 'Confirm your account', 'emails/confirm.jinja2',
        user=current_user, token=token,
    )
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('core.index'))


from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    ValidationError
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from .models import User


class LoginForm(Form):
    email = StringField(
        'Email Address',
        validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField(
        'Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(1, 64), Regexp(
            '^[A-Za-z][A-Za-z0-9_.]*$', 0,
            'Username must have only one letters, numbers, dot or '
            'underscores '
        )]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            EqualTo('password2', message='Passwords must match'),
        ])
    password2 = PasswordField(
        'Confirmation Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

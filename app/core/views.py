
from flask import render_template, session, \
    redirect, url_for, current_app, Blueprint
from app import db
from ..auth.models import User
from .form import NameForm

core = Blueprint('core', __name__, template_folder='templates')


@core.route('/', methods=['GET', 'POST'])
def index():

    form = NameForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if current_app.config['SYSTEM_ADMIN']:
                pass
        else:
            session['known'] = True

        session['name'] = form.name.data
        return redirect(url_for('.index'))

    return render_template(
        'index.jinja2', form=form, name=session.get('name'),
        known=session.get('known', False)
    )

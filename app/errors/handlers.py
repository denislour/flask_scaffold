from flask import Blueprint, render_template

errors = Blueprint('errors', __name__, template_folder="templates")


@errors.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.j2')


@errors.app_errorhandler(500)
def internal_error(error):
    return render_template('500.j2')

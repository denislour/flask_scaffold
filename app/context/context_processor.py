from flask import Blueprint, current_app

context = Blueprint('context', __name__)


@context.app_context_processor
def get_project_name():
    return dict(project_name=current_app.config.get('PROJECT_NAME'))

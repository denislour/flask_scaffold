import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def project_name(name):

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
    os.rename(BASE_DIR, PARENT_DIR + '/' + name)

    with open(os.path.join('config.py'), "r") as f:
        content = f.readlines()
        content_output = []
        for line in content:
            if line.strip().startswith("PROJECT_NAME"):
                line = line.replace(
                    line.split("\"")[1],
                    name.replace("_", " ").title(),
                )
            content_output.append(line)

    with open(os.path.join('config.py'), "w") as f:
        f.writelines(content_output)


if __name__ == '__main__':
    manager.run()

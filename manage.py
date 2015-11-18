#!/usr/bin/env python
import os

from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell

from app import create_app, db
from app.main.models import User, Role

basedir = os.path.abspath(os.path.dirname(__file__))
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db, directory=basedir+'/app/migrations')


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or '234DFGDFdfgtf234234dfgdFGJRETGFHFG456gfhFGH'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Uploads
    UPLOAD_FOLDER = basedir
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    #app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'imuce9@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'N0rthW1ckP4rk)'
    MAIL_SUBJECT_PREFIX = 'test'
    MAIL_SENDER = 'NewBrain Admin <imuce9@gmail.com>'
    MAIL_ADMIN = 'imuce9@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):

    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

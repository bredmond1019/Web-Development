import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = os.environ.get("MAIL_SERVER", 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'false')
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL", 'true')
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    CLIMBR_MAIL_SUBJECT_PREFIX = '[Climbr]'
    CLIMBR_MAIL_SENDER = 'Climbr Admin <bj.redmond19@gmail.com>'
    CLIMBR_ADMIN = os.environ.get('CLIMBR_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RC_SECRET_KEY')
    UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'Climbr/static/uploads')
    CLIMBR_POSTS_PER_PAGE = 12

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql://brandon:flask@localhost:5432/climbr'

config = {
    'development': DevelopmentConfig
}
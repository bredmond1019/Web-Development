import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = os.environ.get("MAIL_SERVER", 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    CLIMBR_MAIL_SUBJECT_PREFIX = '[Climbr]'
    CLIMBR_MAIL_SENDER = 'Climbr Admin <bredmond1019@gmail.com>'
    CLIMBR_ADMIN = os.environ.get('CLIMBR_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql://brandon:flask@localhost:5432/climbr'

config = {
    'development': DevelopmentConfig
}
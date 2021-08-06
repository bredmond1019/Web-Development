import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "H3#6F&3Hhgf6783"
    # MAIL_SERVER = os.environ.get("MAIL_SERVER", 'smtp.gmail.com')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'false')
    # MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL", 'true')
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # FALA_MAIL_SUBJECT_PREFIX = '[Fala]'
    # FALA_MAIL_SENDER = 'Fala Admin <bj.redmond19@gmail.com>'
    # FALA_ADMIN = os.environ.get('FALA_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # RECAPTCHA_PRIVATE_KEY = os.environ.get('RC_SECRET_KEY') or ""
    UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'fala/static/uploads')
    FALA_POSTS_PER_PAGE = 12

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql://bredmond1019:flask@localhost:5432/fala'

config = {
    'development': DevelopmentConfig
}
import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URL") or 'sqlite:///'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "TESTING_DATABASE_URL") or 'sqlite:///'


class ProductionConfig(Config):
    SQLALCHEMY_DATABSASE_URI = os.environ.get("DATABASE_URL") or 'sqlite:///'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig}

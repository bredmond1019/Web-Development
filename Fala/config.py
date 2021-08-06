class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql://bredmond1019:flask@localhost:5432/fala'

config = {'development' : DevelopmentConfig}
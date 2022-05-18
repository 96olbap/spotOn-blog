import os
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://apple:pass123@localhost/postblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(32)
    SECRET_KEY = 'wepukhulu'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
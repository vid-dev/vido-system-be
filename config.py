import os

appData = {
    'DEFAULT_WRITER_PASS' : os.environ.get('DEF_USR_PASS')
}


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    MAIL_MAX_EMAILS = os.environ.get('')
    MAIL_SUPPRESS_SEND = os.environ.get('')
    MAIL_ASCII_ATTACHMENTS = os.environ.get('')
    # SUBJECT_PREFIX = appData['institution_name']
    SQLALCHEMY_TRACK_MODIFICATIONS = True 

    # simplemde confirgurations
    # simplemde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # APP_URL = os.environ.get('APP_URL')


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')


class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config : the parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SUPPRESS_SEND = True
    MAIL_DEBUG = True 
    TESTING = True
    DEBUG = True


config_options = {
    'development' : DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}
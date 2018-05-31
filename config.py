class Config:
    APP_NAME = 'gigzag'
    SECRET_KEY = 'somethingSUPERsecret123'
    ADMIN_NAME = 'administrator'
    
    STATIC_PREFIX_PATH = 'static'
    ALLOWED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'gif']
    MAX_IMAGE_SIZE = 5242880 # 5MB
    MONGODB_HOST = 'mongodb://heroku_99gvrpkn:1ten6nau3lcjjg6j8qkcfden2a@ds139960.mlab.com:39960/heroku_99gvrpkn'
    MONGODB_DB = 'heroku_99gvrpkn'

class DevelopmentConfig(Config):
    DEBUG = True
    
class TestConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False


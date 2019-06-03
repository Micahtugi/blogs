import os
class Config:
    BLOG_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('Tugi')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://micah:tugi@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
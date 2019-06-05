import os
class Config:
    # BLOG_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://micah:tugi@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get("HEROKU_POSTGRESQL_AMBER_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://micah:tugi@localhost/blogs2'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
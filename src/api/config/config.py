import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'this-is-a-secret')
    DEBUG = False
    TESTING = False
    DEMO = False

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    CASSANDRA_HOST = 'db'
    DEMO = True

class TestConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = True
    CASSANDRA_HOST = 'db'

class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = os.getenv('PRODUCTION_SECRET_KEY')
    DEBUG = False
    CASSANDRA_HOST = 'https://db.cue.zone/'
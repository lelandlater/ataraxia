import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'this-is-a-secret')
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    CASSANDRA_HOST = 'cassandra'

class TestConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = True
    CASSANDRA_HOST = 'cassandra'

class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = os.getenv('PRODUCTION_SECRET_KEY')
    DEBUG = False
    CASSANDRA_HOST = 'https://db.cue.zone/'

CASSANDRA_HOST='0.0.0.0'
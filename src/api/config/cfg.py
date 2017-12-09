import os
basedir = os.path.abspath(os.path.dirname(__file__))

CUEAPI_SECRET_KEY = os.getenv("CUEAPI_SECRET_KEY", "this-is-a-secret")
CUEAPI_LOG_CONFIGURATION = os.getenv("CUEAPI_LOG_CONFIGURATION", "")
CASSANDRA_HOST = os.getenv("CASSANDRA_HOST", "cassandra")
DEBUG = os.getenv("DEBUG", False)
TESTING = os.get("TESTING", False)
PRESERVE_CONTEXT_ON_EXCEPTION = True
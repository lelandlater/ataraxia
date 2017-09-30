from api.v0 import create_app
from config import config

app = create_app(config.DevelopmentConfig)

if __name__=="__main__":
    app.run(port=10101, debug=True, use_reloader=False)
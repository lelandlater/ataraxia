import logging
from api.v0 import create_app
from config import config

app = create_app(config.DevelopmentConfig)

log = logging.getLogger('cueapi')
log.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

# add Flask-Script, management functions here

if __name__=="__main__":
    app.run(port=10101, debug=True, use_reloader=False)

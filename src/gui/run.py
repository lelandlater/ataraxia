import logging
from views import index, contact
from flask import Flask

log = logging.getLogger()
log.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

app = Flask(__name__)

app.route('/')(index)
app.route('/contact')(contact)

if __name__=="__main__":
    app.run(port=9000, debug=True, use_reloader=False)
    

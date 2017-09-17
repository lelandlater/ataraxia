from flask import Flask
import logging
from gui import views

log = logging.getLogger()
log.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

app = Flask(__name__, template_folder='gui/templates', static_folder='gui/static')

app.route('/')(views.index)
app.route('/contact')(views.contact)
app.route('/info')(views.info)
app.route('/request_auth')(views.request_auth)
app.route('/access')(views.access)

if __name__=="__main__":
    app.run(port=9000, debug=True, use_reloader=False)
    

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_babel import Babel

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True

csrf = CSRFProtect(app)
Bootstrap(app)

babel = Babel()
babel.init_app(app)

from application.routes import *

if __name__ == '__main__':
    app.run()

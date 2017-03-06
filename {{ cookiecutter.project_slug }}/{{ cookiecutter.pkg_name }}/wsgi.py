import bottle

from .templates import template
from . import settings


bottle.debug(settings.DEBUG)
# Use any upper-cased variables as settings.
settings_dict = {k: v for k, v in vars(settings).items() if k.upper() == k}
app = bottle.Bottle()
app.config.load_dict(settings_dict)


@app.route('/', name='home')
@template('home.html')
def home():
    return {
        'page_title': 'Home',
        'section': 'home',
    }

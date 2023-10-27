from flask import blueprint

api=blueprint('api', __name__, url_prefix='api')

from . import routes
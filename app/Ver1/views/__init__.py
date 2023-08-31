from flask import Blueprint

scheme = Blueprint('scheme', __name__)
blueprint = Blueprint('blueprint', __name__, url_prefix='/api')


from app.Ver1.views.transact import *
from app.Ver1.views.signup import *
from app.Ver1.views.about import *

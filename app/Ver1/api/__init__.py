from flask import Blueprint

blueprint = Blueprint('blueprint', __name__, url_prefix='/api')


from app.Ver1.api.account_interactions import *
from app.Ver1.api.recipe_management import *
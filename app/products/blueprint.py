from flask import Blueprint

products_blueprint = Blueprint("products_blueprint", __name__, url_prefix="/products")

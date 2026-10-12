from flask import Blueprint

orders_blueprint = Blueprint("orders_blueprint", __name__, url_prefix="/orders")

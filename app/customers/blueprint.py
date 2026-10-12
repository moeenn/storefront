import flask
from flask import Blueprint

customers_blueprint = Blueprint(
    "customers_blueprint", __name__, url_prefix="/customers"
)


@customers_blueprint.route("/", methods=["GET"])
def list_customers():
    res = flask.make_response({"message": "not-implemented"})
    return res

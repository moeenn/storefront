#! /bin/env python3

from flask import Flask

from app.customers.blueprint import customers_blueprint
from app.orders.blueprint import orders_blueprint
from app.products.blueprint import products_blueprint

# files in static available at: /static/filename
app = Flask(__name__)
app.register_blueprint(customers_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(orders_blueprint)


if __name__ == "__main__":
    app.run(port=3000, debug=True)

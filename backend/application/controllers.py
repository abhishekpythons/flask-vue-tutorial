from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from .models import Product
from werkzeug.security import generate_password_hash, check_password_hash
from .exts import db
import uuid

controller = Blueprint('controller', __name__)


@controller.route('/', methods=['GET'])
def greetings():
    return """
    Hello, World!
    <form id="form1" action="/products" method="post">
 <input id='name' type="text">
 <input id='link' type="text">
 <input id='bought' type="checkbox">
  <button type="submit" onClick='sub()'>Submit &raquo;</button>
</form>
    """

# fet route handler


@controller.route('/products', methods=['GET', 'POST'])
def all_products():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        new_product = Product(id=uuid.uuid4().hex,
                              name=post_data['name'],
                              link=post_data['link'],
                              quantity=int(post_data['quantity']),
                              bought=post_data['bought'])
        db.session.add(new_product)
        db.session.commit()
        response_object['message'] = "Product Added from Flask!"
    else:
        products = Product.query.filter().all()
        response_object['products'] = []
        for product in products:
            response_object['products'].append(product.serialize)

    return jsonify(response_object)


@controller.route('/products/<product_id>', methods=['PUT', 'DELETE'])
def single_product(product_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        product = Product.query.filter(Product.id == product_id).first()
        product.name = post_data['name']
        product.link = post_data['link']
        product.quantity = int(post_data['quantity'])
        product.bought = post_data['bought']
        db.session.commit()
        response_object['message'] = 'Product Udated!'
    if request.method == "DELETE":
        product = Product.query.filter(Product.id == product_id).first()
        db.session.delete(product)
        db.session.commit()
        response_object['message'] = 'Product Removed!'
    return jsonify(response_object)

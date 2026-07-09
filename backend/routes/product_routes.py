from flask import Blueprint, render_template, abort
from services.product_service import ProductService

product_bp = Blueprint("products", __name__)


@product_bp.route("/products")
def products():

    products = ProductService.get_all_products()

    return render_template(
        "products.html",
        products=products
    )


@product_bp.route("/products/<int:product_id>")
def product_details(product_id):

    product = ProductService.get_product_by_id(product_id)

    if not product:
        abort(404)

    return render_template(
        "product_details.html",
        product=product
    )
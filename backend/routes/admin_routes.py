from flask import Blueprint, render_template
from services.product_service import ProductService

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin/products")
def admin_products():

    products = ProductService.get_all_products()

    return render_template(
        "admin_products.html",
        products=products
    )
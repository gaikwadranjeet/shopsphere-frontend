from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    return render_template("index.html")


@home_bp.route("/contact")
def contact():
    return render_template("contact.html")


@home_bp.route("/login")
def login():
    return render_template("login.html")


@home_bp.route("/cart")
def cart():
    return render_template("cart.html")
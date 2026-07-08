from flask import Flask, render_template
from data.products import products

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/products")
def products_page():
    return render_template(
        "products.html",
        products=products
    )


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


if __name__ == "__main__":
    app.run(debug=True)
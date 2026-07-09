from app import app
from models.product import Product

with app.app_context():

    products = Product.query.all()

    print(f"Total Products: {len(products)}")

    print()

    for product in products:
        print(product.id)
        print(product.name)
        print(product.price)
        print(product.description)
        print("-------------------------")
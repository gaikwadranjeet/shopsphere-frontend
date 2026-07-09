from app import app
from extensions import db
from models.product import Product

products = [
    Product(
        name="Gaming Laptop",
        price=79999,
        description="RTX Gaming Laptop",
        image="laptop.jpg"
    ),
    Product(
        name="Wireless Headphones",
        price=7999,
        description="Noise Cancelling Headphones",
        image="headphones.jpg"
    ),
    Product(
        name="Smart Watch",
        price=9999,
        description="Fitness Smart Watch",
        image="watch.jpg"
    ),
    Product(
        name="Mechanical Keyboard",
        price=5499,
        description="RGB Mechanical Keyboard",
        image="keyboard.jpg"
    )
]

with app.app_context():

    # Clear existing products
    Product.query.delete()

    # Insert fresh products
    db.session.add_all(products)

    db.session.commit()

print("Database seeded successfully!")
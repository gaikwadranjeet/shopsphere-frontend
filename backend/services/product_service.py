from models.product import Product
from flask import abort


class ProductService:

    @staticmethod
    def get_all_products():
        return Product.query.all()


@staticmethod
def get_product_by_id(product_id):
    return Product.query.filter_by(id=product_id).first()


    @staticmethod
    def create_product(product):
        from extensions import db

        db.session.add(product)
        db.session.commit()


    @staticmethod
    def delete_product(product):
        from extensions import db

        db.session.delete(product)
        db.session.commit()
from flask import Flask
from config import Config
from extensions import db
from routes.admin_routes import admin_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

# Import models AFTER db initialization
from models.product import Product

# Import routes
from routes.home_routes import home_bp
from routes.product_routes import product_bp

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(product_bp)
app.register_blueprint(admin_bp)
if __name__ == "__main__":
    app.run(debug=True)
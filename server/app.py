from flask import Flask
from flask_migrate import Migrate
from models import db

# Initialize app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bind SQLAlchemy and Migrate to app
db.init_app(app)
migrate = Migrate(app, db)

# Basic route for testing
@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

# Entry point
if __name__ == '__main__':
    app.run(port=5555, debug=True)

from flask import Flask

# Initialize the app
app = Flask(__name__)

# Import routes after app is initialized
from app.routes import *
from flask import Flask
import os
# Initialize the app
app = Flask(__name__,template_folder=os.path.join(os.getcwd(),'views'), static_folder=os.path.join(os.getcwd(),'static'))

# Import routes after app is initialized
from app.routes import *
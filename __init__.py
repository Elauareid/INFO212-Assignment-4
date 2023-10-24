from flask import Flask

# Initialize the app
app = Flask("project")

# Ensure json responses preserve order
app.json.sort_keys = False

from project.controller import *
# Import the Flask framework to create a web application
from flask import Flask

# Import the aws_wsgi response adapter to convert Flask responses into AWS Lambda-compatible format
from aws_wsgi import response

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ("/") that returns a simple greeting
@app.route("/")
def hello():
    return "Hello from Lambda!"

def handler(event, context):
    return response(app, event, context)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Welcome to DevOps batch-1'

@app.route('/health')
def health():
    return 'Server is up and running'

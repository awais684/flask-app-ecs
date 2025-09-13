# flask-app-ecs
Simple Flask app to be run on ECS

Some projects put the main Flask app in a file called app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from app.py!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
---------

Other projects use a run.py (or sometimes main.py) as the entrypoint.

Often this file imports the Flask app from another module and runs it:

from app import app  # assuming app.py defines "app = Flask(__name__)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

If the project is structured around app.py only → run that.

If there’s a run.py which imports the app and starts it → that’s the file to run.

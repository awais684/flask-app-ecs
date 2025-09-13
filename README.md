# flask-app-ecs
Simple Flask app to be run on ECS


### Using `app.py` directly
Some projects put the main Flask app in a file called **`app.py`**:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from app.py!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### Using `run.py (or main.py)` as entrypoint

Other projects use a run.py (or sometimes main.py) as the entrypoint.

Often this file imports the Flask app from another module and runs it:
```
from app import app  # assuming app.py defines "app = Flask(__name__)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```


✅ Rule of thumb:

If the project is structured around app.py only → run 
```
CMD ["PYTHON", "app.py"}
```

If there’s a run.py which imports the app and starts it → that’s the file to run.
```
CMD ["PYTHON", run.py"]

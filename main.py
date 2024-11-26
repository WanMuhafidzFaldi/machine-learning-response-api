from flask import Flask
from project.routes import register_routes
from mangum import Mangum  # AWS Lambda and API Gateway adapter
import os
from joblib import parallel_backend
from asgiref.wsgi import WsgiToAsgi

# Configure joblib to use the /tmp directory
os.environ["JOBLIB_TEMP_FOLDER"] = "/tmp"

# Optionally, configure parallel backend
with parallel_backend("loky"):
    pass

app = Flask(__name__)
app.config.from_object('project.config.Config')

register_routes(app)

# Wrap the Flask app with WsgiToAsgi to make it ASGI-compatible
asgi_app = WsgiToAsgi(app)

# Lambda handler
lambda_handler = Mangum(asgi_app, lifespan="off")  # This bridges Flask with AWS Lambda

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
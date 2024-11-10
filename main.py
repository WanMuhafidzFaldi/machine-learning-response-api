from flask import Flask
from project.routes import register_routes

app = Flask(__name__)
app.config.from_object('project.config.Config')

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
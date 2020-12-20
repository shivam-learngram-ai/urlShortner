from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from models import db
from routes.url import bp as url_bp

app = Flask(__name__)
CORS(app)

app.config.from_object("config.Config")
app.config["SWAGGER"] = {
    "title": "URL Shortener",
    "description": "This is a simple URL shortener",
    "version": "1.0.0",
}

db.app = app
db.init_app(app)
db.create_all()


app.register_blueprint(url_bp)


@app.route("/")
def helloWorld():
    return "Hello, cross-origin-world!"


swagger = Swagger(app)
if __name__ == "__main__":
    app.run(debug=True)

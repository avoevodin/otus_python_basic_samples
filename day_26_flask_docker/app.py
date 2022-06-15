from flask import Flask, request, render_template
from flask_migrate import Migrate

from day_25_flask_sqla.models.database import db

from day_25_flask_sqla.config import SQLALCHEMY_DB_URI
from day_25_flask_sqla.views.products import products_app

app = Flask(__name__)

app.config.update(
    ENV="development",
    SECRET_KEY="ldkjflds",
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DB_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db.init_app(app)

migrate = Migrate(
    app,
    db,
    compare_type=True,
)

# db.app = app
# or
# with app.app_context():
#     db.create_all()
#     db.drop_all()

app.register_blueprint(products_app, url_prefix="/products")


@app.route("/")
def index_page():
    return render_template("index.html")


@app.get("/hello/")
def hello_name():
    name_world = "World"
    name = request.args.get("name", name_world)
    name = name.strip()
    if not name:
        name = name_world
    return {"message": f"Hello, {name}"}


@app.get("/items/<int:item_id>/")
def get_item(item_id: int):
    return {"item": {"id": item_id}}


@app.get("/items/<item_id>/")
def get_item_string(item_id: str):
    return {"item_id": item_id.upper()}


if __name__ == "__main__":
    app.run(debug=True, port=5050)

from flask import Flask, request, render_template

from views.products import products_app

app = Flask(__name__)

app.config.update(ENV="development", SECRET_KEY="ldkjflds")

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

from fastapi import FastAPI
from pydantic import constr

from users.api import router as users_router
from users.api_async import router as users_router_async

app = FastAPI(title="Sync API")
app.include_router(users_router, prefix="/users/sync")
app.include_router(users_router_async, prefix="/users")


@app.get("/")
def root():
    # 'hel' "lo" ''' wor''' """ld!"""
    """
    ```
    root.__doc__
    'hello world!'

    "GET /"
    ```
    """

    return {"message": "Hello World!!!"}


@app.get("/hello")
# def hello_view(name: str = "OTUS"):
def hello_view(name: constr(min_length=3) = "OTUS"):
    """
    GET /hello?name=OTUS
    :param name:
    :return:
    """
    return {"message": f"Hello {name}"}

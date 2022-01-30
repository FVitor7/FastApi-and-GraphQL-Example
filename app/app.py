from fastapi import FastAPI
from .schema import graphql_app

app = FastAPI()

@app.get("/")
def read_root():
    return {"GraphQl Endpoint": "/graphql"}


app.include_router(graphql_app, prefix='/graphql')
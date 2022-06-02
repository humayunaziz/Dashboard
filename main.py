from fastapi import FastAPI, Body, Depends
import json
from dbutility import DbUtility
from auth_handler import signJWT
from auth_bearer import JWTBearer
from model import PostSchema

app = FastAPI()
posts = []


@app.get("/")
def getData():
    return 'done'


@app.get("/{email}")
def getData(email: str):
    return signJWT(email)


@app.post("/customers", dependencies=[Depends(JWTBearer())])
def getcustomers():
    return DbUtility().getCustomer()


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return posts

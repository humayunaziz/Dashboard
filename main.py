from fastapi import FastAPI
import json

from pydantic import constr
import config
import pyodbc
import pandas as pd

from dbutility import DbUtility

app = FastAPI()


@app.get("/")
def getData():
    return DbUtility().getCustomer()

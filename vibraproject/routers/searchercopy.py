import logging,os
from fastapi import Request
import pandas as pd
from typing import Optional
from fastapi import APIRouter

logging.basicConfig(level=logging.INFO)

router = APIRouter(responses={404: {"description": "Not found"}})

@router.get("/search")
async def search(req: Request):
    columns_names = ["index","name","last_name","mail","gender","game","city"]
    current_working_dir=os.getcwd()
    df = pd.read_csv(f'{current_working_dir}\\vibraProject\\utilidades\\vibra_challenge.csv',names=columns_names)
    df = df.reset_index(drop=True)
    request_args = dict(req.query_params)
    for i in range(len(request_args)):
        request_args[i] = df[request_args]
    df(request_args)
    df2 = pd.DataFrame([request_args],columns=columns_names)
    df2 = df2.reset_index(drop=True)

import logging,os
import pandas as pd
from typing import Optional
from fastapi import APIRouter

logging.basicConfig(level=logging.INFO)

router = APIRouter(responses={404: {"description": "Not found"}})

@router.get("/search")
async def search(
    name: Optional[str] = None,
    last_name:Optional[str] = None,
    city: Optional[str] = None
    ):
    
    current_working_dir=os.getcwd()
    df = pd.read_csv(f'{current_working_dir}\\vibraProject\\utilidades\\vibra_challenge.csv',header=None)

    if name and last_name and city:
        df = df.loc[(df[1]== name) & (df[2] == last_name) & (df[6] == city)]
    elif last_name and city:
        df = df.loc[(df[2] == last_name) & (df[6] == city)]
    elif name and last_name:
        df = df.loc[(df[1] == name) & (df[2] == last_name)]
    elif name and city:
        df = df.loc[(df[1]== name) & (df[6] == city)]
    elif name:
        df = df.loc[df[1]== name]
    elif city:
        df = df.loc[df[6]== city]
    
    print(df)
    return df



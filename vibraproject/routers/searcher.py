"""searcher from csv"""

import logging
import os
from typing import Optional

import pandas as pd
from fastapi import APIRouter

logging.basicConfig(level=logging.INFO)

router = APIRouter(responses={404: {"description": "Not found"}})


@router.get("/search")
async def search(
    name: Optional[str] = None,
    last_name: Optional[str] = None,
    city: Optional[str] = None,
    quantity: int = 0,
):
    """get request to search in csv"""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    df_searcher = pd.read_csv(
        f"{current_dir}/vibra_challenge.csv",
        header=None,
    )

    if name and last_name and city:
        df_searcher = df_searcher.loc[
            (df_searcher[1] == name)
            & (df_searcher[2] == last_name)
            & (df_searcher[6] == city)
        ]
    elif last_name and city:
        df_searcher = df_searcher.loc[
            (df_searcher[2] == last_name) & (df_searcher[6] == city)
        ]
    elif name and last_name:
        df_searcher = df_searcher.loc[
            (df_searcher[1] == name) & (df_searcher[2] == last_name)
        ]
    elif name and city:
        df_searcher = df_searcher.loc[
            (df_searcher[1] == name) & (df_searcher[6] == city)
        ]
    elif name:
        df_searcher = df_searcher.loc[df_searcher[1] == name]
    elif city:
        df_searcher = df_searcher.loc[df_searcher[6] == city]

    print(df_searcher[0:quantity])
    df_to_json = df_searcher[0:quantity].to_json(orient="values")
    return df_to_json

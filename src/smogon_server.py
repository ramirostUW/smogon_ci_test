"""Entry file for SmogonAPI. This file includes all the handlers for all APIs supported"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.static_data_loader import load_pokemon_stats

static_data = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan function that handles data loading before the server starts.
    It will load static data in memory and API handlers can utilize the
    loaded objects for lookup information.
    :param app: FastAPI app
    :return: does not return, will live for the entirety of the server lifespan
    """
    static_data["pokemon_stats_data"] = load_pokemon_stats()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/getPokemonStatsHistorical/{pokemon}")
def get_pokemon_stats_historical(pokemon: str):
    """
    API handler for retrieving Pokemon stats from static Gen1-8 dataset
    :param pokemon: pokemon name
    :return: stats if found
    """
    pokemon_stats_data = static_data["pokemon_stats_data"]
    pokemon_stats = pokemon_stats_data[pokemon]

    print(pokemon_stats)
    response = {}
    if pokemon_stats is None:
        response['status'] = "Failed"
        response['reason'] = "Pokemon not found in Gen 1-8 dataset"
    else:
        response['status'] = "Success"
        response['stats'] = pokemon_stats
    return response

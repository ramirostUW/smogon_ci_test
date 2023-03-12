from contextlib import asynccontextmanager
from fastapi import FastAPI
from .subModules import smogonEndpoints, httpEndpoints, kaggleDataEndpoints

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
app.include_router(smogonEndpoints.router)
app.include_router(httpEndpoints.router)
app.include_router(kaggleDataEndpoints.router)


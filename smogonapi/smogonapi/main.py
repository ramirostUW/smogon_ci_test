# pylint: disable=import-error
"""
This is the root module of our Smogon API. It is a barebones file that
mostly just grabs the endpoints from the appropriate submodules.
"""
#from contextlib import asynccontextmanager
from fastapi import FastAPI
from .submodules import smogon_endpoints, http_endpoints, kaggle_data_endpoints


static_data = {}

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     """
#     Lifespan function that handles data loading before the server starts.
#     It will load static data in memory and API handlers can utilize the
#     loaded objects for lookup information.
#     :param app: FastAPI app
#     :return: does not return, will live for the entirety of the server lifespan
#     """
#     static_data["pokemon_stats_data"] = load_pokemon_stats()
#     yield


#myApp = FastAPI(lifespan=lifespan)
myApp = FastAPI()
myApp.include_router(smogon_endpoints.router)
myApp.include_router(http_endpoints.router)
myApp.include_router(kaggle_data_endpoints.router)

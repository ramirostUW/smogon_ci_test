"""
This submodule contains all of the endpoints that primarily
return data from static datasets.
"""

from fastapi import APIRouter
from .static_data_loader import load_pokemon_stats

router = APIRouter()

@router.get("/getPokemonStatsHistorical/{pokemon}")
def get_pokemon_stats_historical(pokemon: str):
    """
    API handler for retrieving Pokemon stats from static Gen1-8 dataset
    :param pokemon: pokemon name
    :return: stats if found
    """

    #could not get the static data loading to my end.
    #I don't think it's a problem to just read straight from the CSV
    #each time, since scaling this up is outside the scope of hte class
    # pokemon_stats_data = static_data["pokemon_stats_data"]
    pokemon_stats_data = load_pokemon_stats()
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

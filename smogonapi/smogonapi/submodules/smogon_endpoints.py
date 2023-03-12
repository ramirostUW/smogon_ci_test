"""
This module contains all of the endpoints that
primarily return scraped data from Smogon.com.
"""

import json
from fastapi import APIRouter
import requests
from bs4 import BeautifulSoup as bs

router = APIRouter()

@router.get("/charizard")
def get_charizard():
    """
    docstring
    """
    url = "https://www.smogon.com/dex/sm/pokemon/charizard"
    url_page = requests.get(url, timeout=100000)
    soup = bs(url_page.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = bs(script.text, "html.parser")
    smogon_html = script_insides.find("p").text
    first_overview = smogon_html.split("<\\/p>")[0].replace("<\\/a>", "")
    return {"overview": first_overview}

@router.get("/firstOverview")
def get_first_overview(pokemon_name):
    """
    docstring
    """
    url = "https://www.smogon.com/dex/sm/pokemon/" + pokemon_name.lower()
    url_page = requests.get(url, timeout=100000)
    soup = bs(url_page.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = bs(script.text)
    smogon_html = script_insides.find("p").text
    first_overview = smogon_html.split("<\\/p>")[0].replace("<\\/a>", "")
    return {"overview": first_overview}

@router.get("/getJSONGen7")
def get_json(pokemon_name):
    """
    docstring
    """
    url = "https://www.smogon.com/dex/sm/pokemon/" + pokemon_name.lower()
    url_page = requests.get(url, timeout=100000)
    soup = bs(url_page.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = script.text
    return json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs'][2][1]

@router.get("/getJSONGen8")
def get_json_g8(pokemon_name):
    """
    docstring
    """
    url = "https://www.smogon.com/dex/ss/pokemon/" + pokemon_name.lower()
    url_page = requests.get(url, timeout=100000)
    soup = bs(url_page.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = script.text
    return json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs'][2][1]

@router.get("/getGen7Data")
def get_pokemon_data():
    """
    docstring
    """
    url = "https://www.smogon.com/dex/sm/pokemon/charizard"
    url_page = requests.get(url, timeout=100000)
    soup = bs(url_page.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = script.text
    return json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs'][1][1]

from fastapi import APIRouter
import requests
from bs4 import BeautifulSoup as bs
import json

router = APIRouter()

@router.get("/charizard")
def getCharizard():
    url = "https://www.smogon.com/dex/sm/pokemon/charizard"
    urlPage = requests.get(url)
    soup = bs(urlPage.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = bs(script.text, "html.parser")
    smogon_html = script_insides.find("p").text
    first_overview = smogon_html.split("<\\/p>")[0].replace("<\\/a>", "")
    return {"overview": first_overview}

@router.get("/firstOverview")
def getFirstOverview(pokemonName):
    url = "https://www.smogon.com/dex/sm/pokemon/" + pokemonName.lower()
    urlPage = requests.get(url)
    soup = bs(urlPage.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = bs(script.text)
    smogon_html = script_insides.find("p").text
    first_overview = smogon_html.split("<\\/p>")[0].replace("<\\/a>", "")
    return {"overview": first_overview}

@router.get("/getJSONGen7")
def getJSON(pokemonName):
    url = "https://www.smogon.com/dex/sm/pokemon/" + pokemonName.lower()
    urlPage = requests.get(url)
    soup = bs(urlPage.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = script.text
    return json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs'][2][1]

@router.get("/getJSONGen8")
def getJSON(pokemonName):
    url = "https://www.smogon.com/dex/ss/pokemon/" + pokemonName.lower()
    urlPage = requests.get(url)
    soup = bs(urlPage.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = script.text
    return json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs'][2][1]

@router.get("/getGen7Data")
def getPokemonData():
    url = "https://www.smogon.com/dex/sm/pokemon/charizard"
    urlPage = requests.get(url)
    soup = bs(urlPage.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = script.text
    return json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs'][1][1]

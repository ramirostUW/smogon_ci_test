from fastapi import APIRouter
import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as pd

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

@router.get("/getTopPokemon")
def get_top_pokemon(stats, gen):
    url = "https://www.smogon.com/dex/" + gen + "/pokemon/"
    urlPage = requests.get(url)
    soup = bs(urlPage.content, 'html.parser')
    
    script = soup.find_all("script")[1]
    script_insides = script.text

    df = pd.DataFrame(json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs'][1][1]['pokemon'])
    df['average'] = df[stats].mean(axis=1)
    str1 = ' '
    df['formats'] = df['formats'].apply(lambda x: str1.join(x))

    top_pokemon = df.groupby('formats').apply(lambda x: x.nlargest(5, 'average')).set_index('formats')
    return top_pokemon.filter(items=['name'] + stats + ['types', 'abilities', 'average'])

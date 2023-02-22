from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup as bs


app = FastAPI()
 
@app.get("/")
def root ():
  return {"message": "Hello World!"}


@app.get("/charizard")
def getCharizard():
    url = "https://www.smogon.com/dex/sm/pokemon/charizard"
    urlPage = requests.get(url)
    soup = bs(urlPage.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = bs(script.text)
    smogon_html = script_insides.find("p").text
    first_overview = smogon_html.split("<\\/p>")[0].replace("<\\/a>", "")
    return {"overview": first_overview}

    
@app.get("/blastoise")
def getCharizard():
    url = "https://www.smogon.com/dex/sm/pokemon/blastoise"
    urlPage = requests.get(url)
    soup = bs(urlPage.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = bs(script.text)
    smogon_html = script_insides.find("p").text
    first_overview = smogon_html.split("<\\/p>")[0].replace("<\\/a>", "")
    return {"overview": first_overview}


@app.get("/firstOverview")
def getFirstOverview(pokemonName):
    url = "https://www.smogon.com/dex/sm/pokemon/" + pokemonName.lower()
    urlPage = requests.get(url)
    soup = bs(urlPage.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = bs(script.text)
    smogon_html = script_insides.find("p").text
    first_overview = smogon_html.split("<\\/p>")[0].replace("<\\/a>", "")
    return {"overview": first_overview}

# SmogonAPI

Jason Wang, Marques J Chacon, Ramiro Steinmann Petrasso, Yangyang Yao

## Project Type
This project consists of a tool that solves a common problem for users: the inability to programmatically access Smogon data. 

## Goal for the Project
The goal of the project is to create an API that scrapes Smogon Data on the fly and packages it for use in third party applications. The application should be able to allow the user to query for a particular Smogon page like any other API endpoint, and receive the data packaged in JSON or CSV format.

## Questions of Interest
This project does not center around any particular question, but questions of minor interest include what type of data users will query most (I.E. tier data, individual Pokemon data, etc.), and if there's any supplemental data sources that could be scraped and joined with data from Smogon to supplement queries (I.E. Bulbapedia data)

## Data Sources We Will Use:

(The two static datasets will be used to provide static data for basic queries like listing Pokemon in a gen, to avoid making unnecessary scrapes. We have a separate dataset for gens 1-8 and gen 9 because we could not find a complete dataset that went past gen 8, due to the recent release of gen 9). 


- https://smogon.com
- https://www.kaggle.com/datasets/notlucasp/pokemon-gen-18-dataset
- https://www.kaggle.com/datasets/timbuck/pokemon-generation-9-scarlet-violet-datasets

	
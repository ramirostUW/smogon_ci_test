# Milestones
The Smogon API will require the following milestones:
1. **Create Web Page Scraper**
    **Success:** User input commands will scrape the relevant information from Smogon
    1. **Get Pokemon Data**
        **Success:** A user can request the name of a pokemon and generation and get the data from Smogon.
    2. **Grab All Pokemon Within a Tier**
        **Success:** The user requests the tier and generation and the API returns a list of all pokemon found within that tier and generation.
    3. **Get Items**
        **Success:** The user requests a generation and the API returns all available held battle items for that generation.
    4. **Find Most Extreme Pokemon**
        **Success:** The user inputs a stat (Atk, Sp. Atk, Spe, etc.) and the API returns the top 10 pokemon with the highest of that stat. If 2 or more stats are requested, then it returns the pokemon with the highest average base stat total within the requested stats.
2. **Deploy API Endpoints**
    **Success:** Our web scraper will be accessible as an app
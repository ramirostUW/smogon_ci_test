# Use Cases
## Check StrategyDex
**Objective:** The API pulls the Strategy Dex Page for a Pokemon or Item that a user specifies

*API:* Issues a prompt asking whethere the user wants information for a Pokemon or an item.

*User:* Checks "Pokemon" or "Item"

*API:* Issues a prompt asking for what Pokemon or item the user wants to profile. Has additional fields for optional parameters such as generation

*User:* Enters input data for the Pokemon or item they want to profile, including any additional parameters.

*API:* Returns the StrategyDex page for the given Pokemona/item, and generation. If no generation is specified, the most recent generation is returned. If either input is invalid, it returns an error page.

## Get In-Game Items
**Objective:** The API returns the in-game location of the given items that the user specifies

*API:* Issues a prompt asking for the item that the user wants to find

*User:* Enters the name of an item

*API:* Issues a dropdown menu asking what game that the user is interested in finding the item for. The menu should only list eligible games for the item that the user specified. If the user specified an invalid item, an error is thrown.

*User:* Selects the game.

*API:* Returns the location of the item for the game that user specified.

## Create Pokemon Data
**Objective:** The API returns a CSV file of different Pokemon statistics, based on the inputs that the user provides.

*API:* Issues a prompt asking what Pokemon(s) the user wants data for, with an option for "All Pokemon" if no specific Pokemon(s) is specified.

*User:* Enters the Pokemon information

*API:* Issues a prompt for the generation(s) that the user is interested in, with an option for "All Generations" if no specific generation is specified

*User:* Enters the generation(s)

*API:* Scrapes the data from Smogon for the particular Pokemon(s) and generation(s) that the user specified. The resulting CSV file will include the Name of the Pokemon, the generation, their type(s), available Abilities, the competitive tier they are listed in, and their base stats (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed).

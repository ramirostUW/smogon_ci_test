<h1 align="center"> Design Specification </h1>

## Overview
The Smogon API system consist of the following components
* User facing API interface
* Service request handler
* Smogon webpage URL generator
* Smogon webpage crawler

## Software Components Specifications

### Component 1 - User facing API interface
* Name: User facing API interface
* What it does: Defines the API interface for the Smogon API, including input/output data schemas and the function signatures.
* Inputs: N/A since this is an interface
* Outputs: N/A since this is an interface
* Assumptions: Users will be able to directly submit requests to the Smogon API through this interface without any additional setup.

### Component 2 - Service request handler
* Name: Smogon API service request handler
* What it does: Server side code that handles the request to response process, including authentication, throttling, and error handling methods such as auto-retry and error message communication.
* Inputs: Smogon API get Pokémon information request
* Outputs: Smogon API get Pokémon information response
* Assumptions: The application logic can be deployed as a service without additional configurations

### Component 3 - Smogon webpage URL generator
* Name: Smogon webpage URL generator
* What it does: Generates Smogon webpage URL link with given Pokémon name
* Inputs: Pokémon name
* Outputs: Smogon webpage link of the given Pokémon
* Assumptions: The logic of generating Smogon webpage link from Pokémon name is deterministic.

### Component 4 - Smogon webpage crawler
* Name: Smogon webpage crawler
* What it does: Crawls the Smogon webpage and parses the body to extract the Pokémon information that is required to construct the API response
* Inputs: Smogon webpage URL
* Outputs: Detailed Pokémon information with specific format
* Assumptions: The Smogon website is always available and will not throttle

## Interactions

The following diagram depicts the interaction between the listed components

![](https://www.websequencediagrams.com/cgi-bin/cdraw?lz=dGl0bGUgU21vZ29uIEFQSQoKVXNlci0-QVBJIFNlcnZlcjogUG9rZW1vbiBpbmZvcm1hdGlvbiByZXF1ZXN0CgAeCi0-AD8HVVJMIEdlbmVyYXRvcjogUgAkBgA9CXdlYnBhZ2UgVVJMCgAeFABuDlJldHVybgAoFQBvDFdlYiBjcmF3bGVyOiBTdWJtaXQgdwAKCgCBJwggd2l0aAB1BQAmCwCBMAlXZWJzaXRlOiBBY2Nlc3MAgg4IAIEqBwCBJQgAHwcAZBAAHw0gYm9keQBWDgCCORggcGFyc2VkIGZyb20AYgkAgkoMVXMAgXsNAIJ6Ego&s=default)

### Check StrategyDex

*API:* Issues a prompt asking whethere the user wants information for a Pokémon or an item.

*User:* Checks "Pokémon" or "Item"

*API:* Issues a prompt asking for what Pokémon or item the user wants to profile. Has additional fields for optional parameters such as generation

*User:* Enters input data for the Pokémon or item they want to profile, including any additional parameters.

*API:* Returns the StrategyDex page for the given Pokémona/item, and generation. If no generation is specified, the most recent generation is returned. If either input is invalid, it returns an error page.

### Get In-Game Items

*API:* Issues a prompt asking for the item that the user wants to find

*User:* Enters the name of an item

*API:* Issues a dropdown menu asking what game that the user is interested in finding the item for. The menu should only list eligible games for the item that the user specified. If the user specified an invalid item, an error is thrown.

*User:* Selects the game.

*API:* Returns the location of the item for the game that user specified.

### Query Pokémon Data

*API:* Issues a prompt asking what Pokémon(s) the user wants data for, with an option for "All Pokémon" if no specific Pokémon(s) is specified.

*User:* Enters the Pokémon information

*API:* Issues a prompt for the generation(s) that the user is interested in, with an option for "All Generations" if no specific generation is specified

*User:* Enters the generation(s)

*API:* Scrapes the data from Smogon for the particular Pokémon(s) and generation(s) that the user specified. The resulting CSV file will include the Name of the Pokémon, the generation, their type(s), available Abilities, the competitive tier they are listed in, and their base stats (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed).

## Preliminary Plan

**Week 6**
- Determine the goal and scope of the project
- Create README.md and LICENSE file

**Week 7**
- Explore the structure and format of the html pages of Smogon
- Finish user stories and use cases of the API

**Week 8**
- Confirm Python packages to implement the web crawler and deploy the API
- Figure out how to deploy the API
- Prepare for technology review presentation and demo

**Week 9**
- Refine endpoints for FastAPI
- Extract Pokémon gen 1-8 and gen 9 dataset from supplemental data sources
- Add environment and dependency files of the API

**Week 10-11**
- Implement setup.py file
- Create unit tests for the API
- Add documentation of codes and improve code style with pylint
- Finalize design and functional documentation
- Prepare for final project presentation
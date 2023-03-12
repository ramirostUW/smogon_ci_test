## SmogonAPI - Components
The Smogon API system consist of the following components
* User facing API interface
* Service request handler
* Smogon webpage URL generator
* Smogon webpage crawler

The following diagram depicts the interaction between the listed components
![](https://www.websequencediagrams.com/cgi-bin/cdraw?lz=dGl0bGUgU21vZ29uIEFQSQoKVXNlci0-QVBJIFNlcnZlcjogUG9rZW1vbiBpbmZvcm1hdGlvbiByZXF1ZXN0CgAeCi0-AD8HVVJMIEdlbmVyYXRvcjogUgAkBgA9CXdlYnBhZ2UgVVJMCgAeFABuDlJldHVybgAoFQBvDFdlYiBjcmF3bGVyOiBTdWJtaXQgdwAKCgCBJwggd2l0aAB1BQAmCwCBMAlXZWJzaXRlOiBBY2Nlc3MAgg4IAIEqBwCBJQgAHwcAZBAAHw0gYm9keQBWDgCCORggcGFyc2VkIGZyb20AYgkAgkoMVXMAgXsNAIJ6Ego&s=default)

The rest of the doc will contain specifications for each components

### Component 1 - User facing API interface
* Name: User facing API interface
* What it does: Defines the API interface for the Smogon API, including input/output data schemas and the function signatures.
* Inputs: N/A since this is an interface
* Outputs: N/A since this is an interface
* Assumptions: Users will be able to directly submit requests to the Smogon API through this interface without any additional setup.

### Component 2 - Service request handler
* Name: Smogon API service request handler
* What it does: Server side code that handles the request to response process, including authentication, throttling, and error handling methods such as auto-retry and error message communication.
* Inputs: Smogon API get Pokemon information request
* Outputs: Smogon API get Pokemon information response
* Assumptions: The application logic can be deployed as a service without additional configurations

### Component 3 - Smogon webpage URL generator
* Name: Smogon webpage URL generator
* What it does: Generates Smogon webpage URL link with given Pokemon name
* Inputs: Pokemon name
* Outputs: Smogon webpage link of the given Pokemon
* Assumptions: The logic of generating Smogon webpage link from Pokemon name is deterministic.

### Component 4 - Smogon webpage crawler
* Name: Smogon webpage crawler
* What it does: Crawls the Smogon webpage and parses the body to extract the Pokemon information that is required to construct the API response
* Inputs: Smogon webpage URL
* Outputs: Detailed Pokemon information with specific format
* Assumptions: The Smogon website is always available and will not throttle


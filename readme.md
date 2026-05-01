## Arbitrage Betting

The goal of this software is to help users detect risk-free betting opportunities where price discrepancies between bookmakers can be exploited.

To use this project, clone the repository:
```
git clone <your-repo-url>
cd <your-repo-folder>
```

Create and activate a virtual environment using [Pipenv](https://pipenv.pypa.io/en/latest/):
```
pipenv shell
```

Install the required dependencies:
```
pipenv install
```

If needed, you can modify the configuration parameters defined in the `CONSTANTS` file to adjust the behavior of the application. For details on available options and data structure, refer to the [official documentation](https://the-odds-api.com/liveapi/guides/v4/)

Finally, run the script by providing your API key from [The Odds API](https://the-odds-api.com/) as an environment variable:
```
API_KEY=<your-api-key> python main.py
```

### Optional parameters
It is possible to set these optional parameters:
- ```--repeat <minutes>``` repeat the execution every ```<minutes>``` minutes
- ```--threshold <value>``` to show only opportunities with profit greater than or equal to ```<value>```
- ```--mode <append|overwrite>``` to choose whether to append results or overwrite the file

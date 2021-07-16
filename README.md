# Documentation
In this project, I chose Alpha Vantage ( financial market data ) to fetch data from.
This project contains a class to pull data from the Alpha Vantage APIs and a CLI tool to 
facilitate and document the usage of Alpha Vantage APIs.

## How to set up
You need to have installed python3.8 in your computer. Then install poetry.
For installing poetry, I forward you to their documentation https://python-poetry.org/docs/ . 
<br>

Once poetry is installed, you can start using the CLI. <br>

## How to use it.
The entrypoint of the CLI is alphavantage. Write `poetry run alphavantage --help` and you will see
the queries that you can perform.
Output:<br>
```
Usage: alphavantage [OPTIONS] COMMAND [ARGS]...

  Script cli.

Options:
  --help  Show this message and exit.

Commands:
  get-currency-exchange-rate  This API returns the realtime exchange rate...
  get-global-quote            A lightweight alternative to the time...
  get-overview                This API returns the company information,...
  get-time-daily-adjusted     This API returns raw (as-traded) daily...
  get-time-series-intraday    This API returns intraday time series of...

```
<br>
Let's see how to fetch currency exchange rate:<br>
Command: <br>

`poetry run alphavantage get-currency-exchange-rate --help` 
<br>
Output: <br>

```
Usage: alphavantage get-currency-exchange-rate [OPTIONS]

  This API returns the realtime exchange rate for a pair of digital currency
  (e.g., Bitcoin) and physical currency (e.g., USD).

Options:
  -f, --from-currency TEXT  The currency you would like to get the exchange
                            rate for.  [required]
  -t, --to-currency TEXT    The destination currency for the exchange rate.
                            [required]
  -a, --api-key TEXT        Write your api key. You can request one for free
                            at https://www.alphavantage.co/  [default: demo]
  --help                    Show this message and exit.

```
<br>
Now let's fetch some information. If you don't want to get the demo data, you will need to use your
own API key (free api key https://www.alphavantage.co/), and pass it with the "-a" flag.<br>
Command: <br>

`poetry run alphavantage get-currency-exchange-rate -f USD -t EUR -a YOUR_API_KEY`
<br>
Output:<br>

`{'Realtime Currency Exchange Rate': {'1. From_Currency Code': 'EUR', '2. From_Currency Name': 'Euro', '3. To_Currency Code': 'USD', '4. To_Currency Name': 'United States Dollar', '5. Exchange Rate': '1.17956000', '6. Last Refreshed': '2021-07-16 11:56:22', '7. Time Zone': 'UTC', '8. Bid Price': '1.17954100', '9. Ask Price': '1.17960700'}}`
<br>

Now, you can fetch all the different data by making use of the `poetry run alphavantage` command and the `--help` flag, and follow the instructions provided
by the CLI as before.
<br>
In Addition all your queries and their results will be logged in an `output.log` file at the root level of the project.
<br>

## Developer
- Ignacio Gonzalez Betegon


<br>
<br>


## Challenge

1. Choose a public API to collect data from. **Document why you chose this API.**

  - Some suggestions: <https://github.com/public-apis/public-apis>

2. **Use Python to build a class or classes to query your chosen API**. Your code should do the following at a basic level:

  - handle errors
  - write information to a log file
  - be configurable

3. **Document and demonstrate how to set up, install, and run a data pull** using your code.

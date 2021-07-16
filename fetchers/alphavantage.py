import aiohttp
from aiohttp.web_exceptions import HTTPNotFound
from loguru import logger

from core.constants import (
    CURRENCY_EXCHANGE_RATE,
    GLOBAL_QUOTE,
    OVERVIEW,
    TIME_SERIES_DAILY_ADJUSTED,
    TIME_SERIES_INTRADAY,
)
from core.messages import SYMBOL_NOT_FOUND


class Alphavantage:
    def __init__(self):
        self.session = aiohttp.ClientSession
        self.url = "https://www.alphavantage.co"
        self.logger = logger

    def symbol_not_exists(self):
        # If a symbol does not exists, the API returns {}.
        # But I want to capture the error better.
        raise HTTPNotFound(reason=SYMBOL_NOT_FOUND)

    def currency_not_exists(self):
        # If a symbol does not exists, the API returns {}.
        # But I want to capture the error better.
        raise HTTPNotFound(reason=SYMBOL_NOT_FOUND)

    async def get_fundamental_analysis(self, symbol, function=OVERVIEW, api_key="demo"):
        self.logger.add(
            "output.log",
            format="{time} {level} {extra[func]} {extra[symbol]} {message}",
            enqueue=True,
        )
        self.logger = self.logger.bind(func=function, symbol=symbol)
        async with self.session() as session:
            async with session.get(
                f"{self.url}/query?function={function}&symbol={symbol}&apikey={api_key}"
            ) as resp:
                result = await resp.json()
                try:
                    if result:
                        self.logger.info(result)
                        return result
                    self.symbol_not_exists()
                except HTTPNotFound:
                    self.logger.error(SYMBOL_NOT_FOUND)

    async def get_time_series_intraday(
        self, interval, symbol, function=TIME_SERIES_INTRADAY, api_key="demo"
    ):
        self.logger.add(
            "output.log",
            format="{time} {level} {extra[func]} {extra[interval]} {extra[symbol]} {message}",
            enqueue=True,
        )
        self.logger = self.logger.bind(func=function, symbol=symbol, interval=interval)
        async with self.session() as session:
            async with session.get(
                f"{self.url}/query?function={function}&symbol={symbol}&interval={interval}&apikey={api_key}"
            ) as resp:
                result = await resp.json()
                try:
                    if result and 'Error Message' not in result:
                        self.logger.info(result)
                        return result
                    self.symbol_not_exists()
                except HTTPNotFound:
                    self.logger.error(SYMBOL_NOT_FOUND)

    async def get_time_daily_adjusted(
        self, symbol, function=TIME_SERIES_DAILY_ADJUSTED, api_key="api_key"
    ):
        self.logger.add(
            "output.log",
            format="{time} {level} {extra[func]} {extra[symbol]} {message}",
            enqueue=True,
        )
        self.logger = self.logger.bind(func=function, symbol=symbol)
        async with self.session() as session:
            async with session.get(
                f"{self.url}/query?function={function}&symbol={symbol}&apikey={api_key}"
            ) as resp:
                result = await resp.json()
                try:
                    if result and "Error Message" not in result:
                        self.logger.info(result)
                        return result
                    self.symbol_not_exists()
                except HTTPNotFound:
                    self.logger.error(SYMBOL_NOT_FOUND)

    async def get_global_quote(self, symbol, function=GLOBAL_QUOTE, api_key="demo"):
        self.logger.add(
            "output.log",
            format="{time} {level} {extra[func]} {extra[symbol]} {message}",
            enqueue=True,
        )
        self.logger = self.logger.bind(func=function, symbol=symbol)
        async with self.session() as session:
            async with session.get(
                f"{self.url}/query?function={function}&symbol={symbol}&apikey={api_key}"
            ) as resp:
                result = await resp.json()
                try:
                    if result and "Global Quote" in result and result["Global Quote"]:
                        self.logger.info(result)
                        return result
                    self.symbol_not_exists()
                except HTTPNotFound:
                    self.logger.error(SYMBOL_NOT_FOUND)

    async def get_currency_exchange_rate(
        self, from_currency, to_currency, function=CURRENCY_EXCHANGE_RATE, api_key="demo"
    ):
        self.logger.add(
            "output.log",
            format="{time} {level} {extra[func]} {extra[from_currency]} {extra[to_currency]} {message}",
            enqueue=True,
        )
        self.logger = self.logger.bind(
            func=function, from_currency=from_currency, to_currency=to_currency
        )
        async with self.session() as session:
            async with session.get(
                f"{self.url}/query?function={function}&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}"
            ) as resp:
                result = await resp.json()
                try:
                    if result and "Error Message" not in result:
                        self.logger.info(result)
                        return result
                    self.currency_not_exists()
                except HTTPNotFound:
                    self.logger.error(result)

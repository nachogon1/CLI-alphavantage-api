import asyncclick as click

from fetchers.alphavantage import Alphavantage


@click.group()
@click.pass_context
async def alphavantage(ctx):
    """Script cli."""
    ctx.obj = Alphavantage()


@alphavantage.command()
@click.option("--symbol", "-s", required=True, help="Symbol of the company. e.g. IBM.")
@click.option(
    "--api-key",
    "-a",
    default="demo",
    required=False,
    help="Write your api key. You can request one for free at https://www.alphavantage.co/",
)
@click.pass_context
async def get_overview(ctx, api_key, symbol):
    """This API returns the company information, financial ratios, and other key metrics for the equity specified.
    Data is generally refreshed on the same day a company reports its latest earnings and financials."""
    await ctx.obj.get_fundamental_analysis(api_key=api_key, symbol=symbol)


@alphavantage.command()
@click.option("--symbol", "-s", required=True, help="Symbol of the company. e.g. IBM.")
@click.option(
    "--interval",
    "-i",
    required=True,
    type=click.Choice(
        ["1min", "5min", "15min", "30min", "60min"], case_sensitive=False
    ),
    show_choices=True,
    help="Interval between two consecutive data points in the time series. ",
)
@click.option(
    "--api-key",
    "-a",
    default="demo",
    required=False,
    help="Write your api key. You can request one for free at https://www.alphavantage.co/",
)
@click.pass_context
async def get_time_series_intraday(ctx, api_key, interval, symbol):
    """This API returns intraday time series of the equity specified,
    covering extended trading hours where applicable
    (e.g., 4:00am to 8:00pm Eastern Time for the US market)."""
    await ctx.obj.get_time_series_intraday(
        api_key=api_key, interval=interval, symbol=symbol
    )


@alphavantage.command()
@click.option("--symbol", "-s", required=True, help="Symbol of the company. e.g. IBM.")
@click.option(
    "--api-key",
    "-a",
    default="demo",
    required=False,
    help="Write your api key. You can request one for free at https://www.alphavantage.co/",
)
@click.pass_context
async def get_time_daily_adjusted(ctx, api_key, symbol):
    """This API returns raw (as-traded) daily open/high/low/close/volume values,
    daily adjusted close values,
    and historical split/dividend events of the global equity specified,
    covering 20+ years of historical data."""
    await ctx.obj.get_time_daily_adjusted(api_key=api_key, symbol=symbol)


@alphavantage.command()
@click.option("--symbol", "-s", required=True, help="Symbol of the company. e.g. IBM.")
@click.option(
    "--api-key",
    "-a",
    default="demo",
    required=False,
    help="Write your api key. You can request one for free at https://www.alphavantage.co/",
)
@click.pass_context
async def get_global_quote(ctx, api_key, symbol):
    """A lightweight alternative to the time series APIs,
    this service returns the price and volume information for a security of your choice."""
    await ctx.obj.get_global_quote(api_key=api_key, symbol=symbol)


@alphavantage.command()
@click.option(
    "--from-currency",
    "-f",
    required=True,
    help="The currency you would like to get the exchange rate for. e.g. EUR",
)
@click.option(
    "--to-currency",
    "-t",
    required=True,
    help="The destination currency for the exchange rate. e.g. USD",
)
@click.option(
    "--api-key",
    "-a",
    default="demo",
    show_default=True,
    required=False,
    help="Write your api key. You can request one for free at https://www.alphavantage.co/",
)
@click.pass_context
async def get_currency_exchange_rate(ctx, api_key, to_currency, from_currency):
    """
    This API returns the realtime exchange rate for a pair of digital currency (e.g., Bitcoin)
    and physical currency (e.g., USD)."""
    await ctx.obj.get_currency_exchange_rate(
        api_key=api_key, to_currency=to_currency, from_currency=from_currency
    )

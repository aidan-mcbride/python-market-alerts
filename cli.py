import click

import main

defaults = dict(
    source="https://www.jmbullion.com/charts/silver-prices/",
    interval=900,
    # limit=1.00,
    # side="above",
)


@click.command()
@click.option(
    "-i",
    "--interval",
    default=defaults["interval"],
    help="Number of seconds to wait between checking price. Default is 15 minutes(900 seconds)",
)
@click.option(
    "-l",
    "--limit",
    required=True,
    type=float,
    help="Spot price of silver at which to be notified",
)
@click.option(
    "-s",
    "--side",
    required=True,
    type=str,
    help="either 'above' or 'below' - check that current price is above or below the given limit",
)
def run(interval: int, limit: float, side: str, source: str = defaults["source"]):
    """
    take inputs via CLI options
    launch application with given options
    """

    main.check_price_periodically(
        interval=interval, source=source, limit=limit, side=side
    )


if __name__ == "__main__":
    run()

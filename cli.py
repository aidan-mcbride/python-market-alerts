import click

import main

# hard-coded global source,
# since right now there is no support for scraping multiple sources
source = "https://www.jmbullion.com/charts/silver-prices/"


@click.command()
@click.option(
    "--interval",
    default=900,
    help="Number of seconds to wait between checking price. Default is 15 minutes(900 seconds)",
)
@click.option("--limit", default=1.00, help="Price at which to be notified")
@click.option(
    "--side",
    default="above",
    help="either 'above' or 'below' - check that current price is above or below the given limit",
)
def run(interval: int, limit: float, side: str):
    """
    take inputs via CLI options
    launch application with given options
    """
    global source
    main.check_price_periodically(
        interval=interval, source=source, limit=limit, side=side
    )


if __name__ == "__main__":
    run()

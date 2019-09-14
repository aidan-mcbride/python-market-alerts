"""
Entire Application is in this file.

Because the whole thing is really quite simple.
"""

import os
import subprocess

import requests
from bs4 import BeautifulSoup

# hard-coded global source,
# since right now there is no support for scraping multiple sources
source = "https://www.jmbullion.com/charts/silver-prices/"


def get_page_content(url: str) -> str:
    """retrieve html from a given url"""
    rv = requests.get(url)
    html: str = rv.text
    return html


def html_to_soup(html: str) -> BeautifulSoup:
    """turns a string of HTML into a soup"""
    return BeautifulSoup(html, "html.parser")


def extract_silver_price(soup: BeautifulSoup) -> float:
    """extracts the price of silver as a float from a soup"""
    result = soup.find("div", {"id": "sounce"})
    price = float(result.string)
    return price


def compare_to_limit(price: float, limit: float, side: str) -> bool:
    """
    checks if a given price has crossed a threshold in a given direction

    price: the price to check
    limit: the threshold
    direction: string, either 'above' or 'below', where price should be in relation to limit.
    """
    if side == "above":
        return price > limit
    elif side == "below":
        return price < limit
    else:
        raise ValueError("'side' must be 'above' or 'below'")


def send_notification(header: str = "no header set", message: str = "no message set"):
    """
    Push a notification to the user's ubuntu desktop using
    ubuntu notify-send in a subprocess call.

    header: the header of the notification
    message: the body of the notification
    """
    notification = [
        "notify-send",
        header,
        message,
        "--urgency=critical",
        "--icon={}".format(os.path.abspath("icon.svg")),
    ]
    subprocess.call(notification)


def get_current_price(source: str) -> float:
    """
    get the spot price of silver from given source
    only works with one source right now.
    """
    html = get_page_content(source)
    soup = html_to_soup(html)
    silver_price = extract_silver_price(soup)
    return silver_price


def create_source_name(source: str) -> str:
    """returns a human-readable name for a source from a given url"""
    # remove http:// or https://
    if source.startswith("https://"):
        source = source.split("https://")[1]
    if source.startswith("http://"):
        source = source.split("http://")[1]
    # remove 'www.' if present
    if source.startswith("www."):
        source = source.split("www.")[1]
    source = source.split("/")[0]
    return source


def check_price(source: str, limit: float, side: str):
    """
    gets the current price of silver,
    checks current price against set limit,
    sends notification of limit reached
    """
    silver_price: float = get_current_price(source)
    try:
        if compare_to_limit(price=silver_price, limit=limit, side=side):
            source_name = create_source_name(source)
            header: str = "Silver spot price: ${}".format(silver_price)
            message: str = "{} is reporting that silver is currently priced at ${} per ounce".format(
                source_name, silver_price
            )
            send_notification(header=header, message=message)
    except ValueError as error:
        return error


if __name__ == "__main__":
    """
    Run program
    """
    check_price(source=source, limit=20.00, side="above")

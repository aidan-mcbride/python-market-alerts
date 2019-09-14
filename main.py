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
    html = get_page_content(source)
    soup = html_to_soup(html)
    silver_price = extract_silver_price(soup)
    return silver_price


if __name__ == "__main__":
    """
    Run program
    """
    print(get_current_price(source))

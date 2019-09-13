"""
Entire Application is in this file.

Because the whole thing is really quite simple.
"""

import requests
from bs4 import BeautifulSoup


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


if __name__ == "__main__":
    """
    Run program
    """
    url = "https://www.jmbullion.com/charts/silver-prices/"

    html = get_page_content(url)
    soup = html_to_soup(html)
    silver_price = extract_silver_price(soup)
    print(silver_price)

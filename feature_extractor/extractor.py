import requests
from bs4 import BeautifulSoup


def fetch_website(url):
    """
    Fetch website HTML content.
    """

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return BeautifulSoup(response.text, "lxml")
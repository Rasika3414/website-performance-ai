import requests
from bs4 import BeautifulSoup


def fetch_website(url):
    """
    Fetch website HTML content.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return BeautifulSoup(response.text, "lxml")


def get_page_size(url):
    """
    Get website page size in bytes.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return len(response.content)


def get_compression_type(url):
    """
    Detect website compression type.
    """
    response = requests.get(url, timeout=10)

    encoding = response.headers.get("Content-Encoding", "")

    if "br" in encoding:
        return "Brotli"
    elif "gzip" in encoding:
        return "Gzip"
    else:
        return "None"


def get_cache_control(url):
    """
    Get Cache-Control header.
    """
    response = requests.get(url, timeout=10)

    cache_control = response.headers.get("Cache-Control")

    if cache_control:
        return cache_control

    return "Not Set"
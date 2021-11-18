import requests
import logging


def get(url):
    """Return GET request"""
    logging.debug("Return GET request")
    return requests.get(url)


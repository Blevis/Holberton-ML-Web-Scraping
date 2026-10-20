#!/usr/bin/env python3
"""0-fetch_html.py"""
import requests


def fetch_html(url, headers=None, timeout=10):
    """Fetch a web page and return its HTML as text.

    Raises requests.HTTPError on any status >= 400.
    """
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text

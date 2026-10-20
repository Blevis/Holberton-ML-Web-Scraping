#!/usr/bin/env python3
"""2-scrape_paginated.py"""
from bs4 import BeautifulSoup
import time
from urllib import parse
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """Scrape all pages of quotes by following the "Next" link.

    Returns a combined list of quote dicts (same format as scrape_basic).
    """
    all_quotes = []
    url = base_url

    while url:
        all_quotes.extend(scrape_basic(url))

        soup = BeautifulSoup(fetch_html(url), "html.parser")
        next_li = soup.find("li", class_="next")
        link = next_li.find("a") if next_li else None

        if link and link.get("href"):
            url = parse.urljoin(url, link["href"])
            time.sleep(1)
        else:
            url = None

    return all_quotes

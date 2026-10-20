#!/usr/bin/env python3
"""1-scrape_basic.py"""
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Scrape the first page of quotes from quotes.toscrape.com.

    Returns a list of dicts with keys: text, author, tags.
    """
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    quotes = []
    for block in soup.find_all("div", class_="quote"):
        text = block.find("span", class_="text").get_text()
        author = block.find("small", class_="author").get_text()
        tags = [a.get_text() for a in block.find_all("a", class_="tag")]
        quotes.append({"text": text, "author": author, "tags": tags})

    return quotes

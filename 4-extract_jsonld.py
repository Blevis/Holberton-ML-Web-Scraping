#!/usr/bin/env python3
"""4-extract_jsonld.py"""
import json
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Extract quotes from JSON-LD blocks embedded in a page.

    Returns a list of dicts with keys: text, author, tags.
    """
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    quotes = []
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
        except json.JSONDecodeError:
            continue

        items = data if isinstance(data, list) else [data]
        for item in items:
            if not isinstance(item, dict) or item.get("@type") != "Quote":
                continue

            keywords = item.get("keywords", [])
            if isinstance(keywords, str):
                keywords = [
                    k.strip() for k in keywords.split(",") if k.strip()
                    ]

            quotes.append({
                "text": item.get("text"),
                "author": item.get("author", {}).get("name"),
                "tags": keywords,
            })

    return quotes

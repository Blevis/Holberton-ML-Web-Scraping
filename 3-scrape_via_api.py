#!/usr/bin/env python3
"""3-scrape_via_api.py"""
import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Scrape all quotes from the site's JSON API.

    Returns a list of dicts with keys: text, author, tags.
    """
    quotes = []
    page = 1

    while True:
        url = f"{base_url.rstrip('/')}/api/quotes?page={page}"
        payload = json.loads(fetch_html(url))

        for q in payload.get("quotes", []):
            quotes.append({
                "text": q["text"],
                "author": q["author"]["name"],
                "tags": q["tags"],
            })

        if not payload.get("has_next"):
            break
        page += 1

    return quotes

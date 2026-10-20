#!/usr/bin/env python3
"""5-login_and_scrape.py"""
import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in with a CSRF-protected form, then scrape the quotes page.

    Returns a list of dicts with keys: text, author, tags.
    """
    session = requests.Session()

    resp = session.get(login_url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    token = soup.find("input", attrs={"name": "csrf_token"})["value"]

    payload = {"username": user, "password": pwd, "csrf_token": token}
    resp = session.post(login_url, data=payload, timeout=10)
    resp.raise_for_status()

    home_url = login_url.rsplit("/login", 1)[0] + "/"
    resp = session.get(home_url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    quotes = []
    for block in soup.find_all("div", class_="quote"):
        text = block.find("span", class_="text").get_text()
        author = block.find("small", class_="author").get_text()
        tags = [a.get_text() for a in block.find_all("a", class_="tag")]
        quotes.append({"text": text, "author": author, "tags": tags})

    return quotes

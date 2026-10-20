#!/usr/bin/env python3
"""8-scroll_and_scrape.py"""
import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll an infinite-scroll page to the end and scrape all products.

    Returns a list of unique dicts with keys: title, price, description,
    rating. Uniqueness is based on the (title, price) pair.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)

        last_height = driver.execute_script(
            "return document.body.scrollHeight")
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause)
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height <= last_height:
                break
            last_height = new_height

        products = []
        seen = set()
        for card in driver.find_elements("css selector", "div.thumbnail"):
            title = card.find_element(
                "css selector", "a.title").get_attribute("title")
            price = card.find_element("css selector", "h4.price").text

            key = (title, price)
            if key in seen:
                continue
            seen.add(key)

            description = card.find_element(
                "css selector", "p.description").text
            rating = len(card.find_elements(
                "css selector", ".ratings .ws-icon-star"))

            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": rating,
            })

        return products
    finally:
        driver.quit()

#!/usr/bin/env python3
"""6-products_list.py"""
import time
from selenium import webdriver


def scrape_products(url):
    """Scrape a static product category page with headless Chrome.

    Returns a list of dicts with keys: title, price, description, rating.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(1)

        products = []
        for card in driver.find_elements("css selector", "div.thumbnail"):
            title = card.find_element(
                "css selector", "a.title").get_attribute("title")
            price = card.find_element("css selector", "h4.price").text
            description = card.find_element(
                "css selector", "p.description").text
            rating = card.find_element(
                "css selector", ".ratings p[data-rating]"
            ).get_attribute("data-rating")

            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": int(rating),
            })

        return products
    finally:
        driver.quit()


# Alias: 6-main.py imports `scrape_products_list` from this module
scrape_products_list = scrape_products
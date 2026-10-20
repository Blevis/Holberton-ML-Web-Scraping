#!/usr/bin/env python3
"""7-product_detail.py"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_product_detail(url, delay=2.0):
    """Scrape a single product detail page with headless Chrome.

    Waits `delay` seconds after loading, then returns a dict with
    keys: title, price, description, rating.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(delay)

        caption = driver.find_element(By.CSS_SELECTOR, ".caption")
        h4s = caption.find_elements(By.CSS_SELECTOR, "h4")

        title = h4s[1].text
        price = caption.find_element(By.CSS_SELECTOR, "h4.price").text
        description = caption.find_element(
            By.CSS_SELECTOR, "p.description").text
        rating = len(driver.find_elements(
            By.CSS_SELECTOR, ".ratings .ws-icon-star"))

        return {
            "title": title,
            "price": price,
            "description": description,
            "rating": rating,
        }
    finally:
        driver.quit()

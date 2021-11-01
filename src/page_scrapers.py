#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Helper functions for scraping search results or listings."""


# pylint: disable=broad-except,too-many-statements,too-many-locals

import os
import re
import time
from random import uniform

import pandas as pd
from bs4 import BeautifulSoup

import src.bs4_helpers as bsh
from src.failure_records import dict_failed_extraction_from_listing_page
from src.utils import export_to_csv, save_to_parquet_file


def scrape_single_page_search_results(driver, raw_data_dir, verbose=False):
    """Scrape a single page of search results."""
    search_results_div = driver.find_elements_by_xpath(
        './/div[@id="search_resultsRows"]/a'
    )
    d_search_results = []
    current_page_num = driver.current_url.split("&page=")[-1]
    try:
        # Verify some listings on page
        assert len(search_results_div) > 0
        try:
            for k, search_result in enumerate(search_results_div):
                listing_info = search_result.find_element_by_xpath(
                    './/div[@class="responsive_search_name_combined"]'
                )

                # Get title
                title_os = listing_info.find_element_by_tag_name("div")
                title = title_os.find_element_by_class_name("title").text

                # Get app_id and listing URL
                app_id = search_result.get_attribute("data-ds-appid")
                url = f"https://store.steampowered.com/app/{app_id}/{title}/"

                # Get supported platforms
                try:
                    platform_spans = title_os.find_element_by_tag_name(
                        "p"
                    ).find_elements_by_tag_name("span")
                    platform_names = ",".join(
                        [
                            p.get_attribute("class").split(" ")[-1]
                            for p in platform_spans
                        ]
                    )
                except Exception:
                    platform_names = [None, None, None]

                # Get release date
                try:
                    xpath = (
                        './/div[@class="col search_released '
                        'responsive_secondrow"]'
                    )
                    rel_date = listing_info.find_element_by_xpath(xpath)
                    release_date = rel_date.text
                except Exception:
                    release_date = None

                # Get discount percent
                xpath_discount_price = (
                    './/div[contains(@class,"search_price_discount_'
                    'combined")]/div'
                )
                discount_price = listing_info.find_elements_by_xpath(
                    xpath_discount_price
                )
                discount_pct = (
                    discount_price[0].text if discount_price[0].text else None
                )

                # Get original and (if available) discounted price
                try:
                    xpath_prices_outer = (
                        './/div[contains(@class,"search_price_discount_'
                        'combined")]'
                    )
                    xpath_prices_inner = (
                        './/div[contains(@class,"col search_price '
                        'discounted")]'
                    )
                    price = listing_info.find_element_by_xpath(
                        xpath_prices_outer
                    ).find_element_by_xpath(xpath_prices_inner)
                    price = price.text
                    original_price, discount_price = price.split("\n")
                except Exception:
                    original_price = (
                        discount_price[1].text
                        if discount_price[1].text
                        else None
                    )
                    discount_price = None
                if verbose:
                    print(
                        current_page_num,
                        k + 1,
                        title,
                        app_id,
                        platform_names,
                        release_date,
                        discount_pct,
                        original_price,
                        discount_price,
                    )
                d_search_results.append(
                    {
                        "page": current_page_num,
                        "listing_counter": k + 1,
                        "title": title,
                        "url": url,
                        "platform_names": platform_names,
                        "release_date": release_date,
                        "discount_pct": discount_pct,
                        "original_price": original_price,
                        "discount_price": discount_price,
                    }
                )
            print(
                "Retrieved listings from search results page "
                f"{current_page_num}."
            )
        except Exception:
            d_search_results.append(
                {
                    "page": current_page_num,
                    "listing_counter": k + 1,
                    "title": None,
                    "url": None,
                    "platform_names": None,
                    "release_date": None,
                    "discount_pct": None,
                    "original_price": None,
                    "discount_price": None,
                }
            )
            print(
                "Error retrieving listings from search results page "
                f"{current_page_num}."
            )
    except Exception:
        # Return failure record if page is blank with no listings
        d_search_results = [
            {
                "page": current_page_num,
                "listing_counter": k + 1,
                "title": None,
                "url": None,
                "platform_names": None,
                "release_date": None,
                "discount_pct": None,
                "original_price": None,
                "discount_price": None,
            }
            for _ in range(25)
        ]
        print("No listings on search results page " f"{current_page_num}.\n")
    # Convert list of dicts into DataFrame
    df_single_page_search_results_single_page = pd.DataFrame.from_records(
        d_search_results
    )
    timestr = time.strftime("%Y%m%d_%H%M%S")
    parquet_filepath = os.path.join(
        raw_data_dir,
        f"search_results_page_{current_page_num}_{timestr}.parquet",
    )
    # Export to CSV file
    if not os.path.exists(parquet_filepath):
        save_to_parquet_file(
            [df_single_page_search_results_single_page], [parquet_filepath]
        )
        print(f"Exported search results for page {current_page_num}.\n")
    else:
        print(
            "File was found with search results information for page "
            f"{current_page_num}. Did nothing.\n"
        )


def scrape_listing(driver, listing_num, page_num, raw_data_dir):
    """Scrape a single listing."""
    print(f"Starting with listing {listing_num}")
    start_time = time.time()
    time.sleep(uniform(1, 3))

    # Get page source
    game_page_source = driver.page_source

    # Try to get the title of the game (if title is visible, then scrape)
    try:
        # Scrape title
        details_block = driver.find_element_by_xpath(
            './/div[@id="genresAndManufacturer"]'
        )
        game_title = (
            details_block.text.lower()
            .split("\ngenre: ")[0]
            .split("title: ")[-1]
            .title()
        )
        game_title = re.sub(r"\W+", "", game_title.replace(" ", "_"))
        print(f"Scraped game title for listing {listing_num} ({game_title})")

        # Scrape listing attributes
        game_soup = BeautifulSoup(game_page_source, "html.parser")
        try:
            listing_details = bsh.scrape_game_listing(game_soup)
            print(f"Scraped listing {listing_num}")
        except Exception:
            listing_details = dict_failed_extraction_from_listing_page()
            print(f"Error with listing {listing_num}. Used failure record.")

        # Write to disk
        export_to_csv(
            (
                pd.DataFrame.from_records([listing_details])
                .assign(page_num=page_num)
                .assign(listing_num=listing_num)
            ),
            raw_data_dir,
            f"p{page_num}_l{listing_num}_{game_title.replace(' ', '_')}",
        )
    except Exception:
        try:
            collection_text = driver.find_element_by_xpath(
                './/h2[@class="no_margin"]'
            ).text.lower()
            if collection_text != "items included in this package":
                print("Listing is collection.")
            else:
                print(f"Listing looks like collection: got {collection_text}")
        except Exception:
            print("Listing is not single game or collection.")

    duration = time.time() - start_time
    print(f"Done with listing {listing_num} in {duration:.3f} sec.")
    return driver

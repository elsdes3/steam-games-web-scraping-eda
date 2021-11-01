#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Helper functions for scraping a single listing with beautifulsoup."""


# pylint: disable=invalid-name,broad-except


import os

import numpy as np
import pandas as pd

from src.utils import regex_get_num_from_str


def get_price_from_listings_page(soup):
    """Get listing price from search results page."""
    price = soup.find("div", class_="responsive_search_name_combined")
    try:
        try:
            price = price.find(
                "div", {"class": "col search_price responsive_secondrow"}
            ).text.strip()
            sale = False
        except Exception:
            price = price.find(
                "div",
                {"class": "col search_price discounted responsive_secondrow"},
            ).text.strip()
            sale = True
        price = price.split("$ ", 1)[-1].replace("CDN$ ", ", ")
        if price == "":
            price = None
            sale = None
    except Exception:
        price = None
        sale = None
    return [price, sale]


def get_overall_review_rating(soup):
    """Get rating for listing from listing page."""
    try:
        try:
            overall = soup.find("span", {"class": "game_review_summary"}).text
        except Exception:
            overall_div = soup.find("div", {"class": "summary_section"})
            overall_div_span = overall_div.find_all("span")
            overall = overall_div_span[0].text
    except Exception:
        overall = np.nan
    return overall


def get_pct_overall_review_rating(soup):
    """Get percent and number of reviews used in rating from listing page."""
    try:
        overall_div = soup.find("div", {"class": "summary_section"})
        overall_div_span = overall_div.find_all("span")
        overall_div_span_text = overall_div_span[0]["data-tooltip-html"]
        assert "Need more user reviews" not in overall_div_span_text
    except Exception:
        pct_overall, threshold_used = [np.nan, np.nan]
    else:
        pct_overall = float(overall_div_span_text.split("%")[0])
        threshold_used = overall_div_span_text.split("for this game are ")[
            1
        ].replace(".", "")
    return [pct_overall, threshold_used]


def get_pct_overall_review_rating_language_filtered(soup):
    """Get lang. pct and num of reviews used in rating from listing page."""
    try:
        overall_div = soup.find(
            "div", {"class": "user_reviews_filter_score visible"}
        ).find("div")
        overall_div_span = overall_div.find_all("span")
        overall_div_span_text = overall_div_span[-1]["data-tooltip-html"]
        assert "Need more user reviews" not in overall_div_span_text
    except Exception:
        pct_overall, threshold_used = [np.nan, np.nan]
    else:
        pct_overall = float(overall_div_span_text.split("%")[0])
        threshold_used = overall_div_span_text.split("for this game are ")[
            1
        ].replace(".", "")
    # print(pct_overall, threshold_used)
    return [pct_overall, threshold_used]


def get_sub_review_counts(soup, review_stats):
    """Get number of each type of user review from listing page."""
    for r_type in [
        "review_type_positive",
        "review_type_negative",
        "review_language_mine",
    ]:
        try:
            r_object = soup.find("label", {"for": r_type})
            review_num = str(
                r_object.find("span", {"class": "user_reviews_count"}).text
            )
            num_reviews_int = regex_get_num_from_str(review_num)
        except Exception:
            num_reviews_int = np.nan
        review_stats.update({r_type: num_reviews_int})
        # print(r_type, num_reviews_int)
    return review_stats


def get_all_reviews_count(soup):
    """Get number of user reviews, in all languages, from listing page."""
    try:
        try:
            r_object = soup.find("label", {"for": "review_type_all"})
            review_num = str(
                r_object.find("span", {"class": "user_reviews_count"}).text
            )
            num_reviews_int = regex_get_num_from_str(review_num)
        except Exception:
            overall = soup.find("div", {"class": "summary_section"})
            overall_span = overall.find_all("span")
            overall_span_text = overall_span[1].text
            num_reviews_int = int(regex_get_num_from_str(overall_span_text))
    except Exception:
        num_reviews_int = np.nan
    return num_reviews_int


def get_release_summary_details(soup, listing_info):
    """Get essential release information from listing page."""
    for field in [
        "Title",
        "Genre",
        "Release Date",
        "Early Access Release Date",
        "Developer",
        "Publisher",
        "Franchise",
    ]:
        block_text = (
            soup.find("div", {"class": "details_block"})
            .text.strip()
            .replace(":\n", ": ")
            .replace("\n\n", "\n")
            .replace("\n\n", "\n")
        )
        block_text_value = block_text.partition(f"{field}: ")[-1]
        field_val = (
            np.nan if not block_text_value else block_text_value.split("\n")[0]
        )
        listing_info[field] = field_val
    return listing_info


def get_languages(soup, listing_info):
    """Get languages supported by listing from listing page."""
    df_lang = pd.read_html(
        str(soup.find("div", {"id": "languageTable"}).find("table")),
        displayed_only=False,
    )[0]
    langs_str = ", ".join(df_lang["Unnamed: 0"].tolist())
    listing_info["languages"] = langs_str
    listing_info["num_languages"] = len(df_lang)
    return listing_info


def get_platforms(soup):
    """Get platforms supported by listing from listing page."""
    try:
        platform_spans = soup.find(
            "div", class_="game_area_purchase_platform"
        ).find_all("span")
        platforms = [
            span
            for platform_span in platform_spans
            for span in platform_span["class"]
            if span != "platform_img"
        ]
        # print(platform_spans)
        platforms_str = ", ".join(platforms)
    except Exception:
        platforms_str = "Unknown"
    return platforms_str


def get_user_defined_tags(soup):
    """Get user-created listing tags from listing page."""
    try:
        tags = [
            t.text.strip()
            for t in soup.find("div", class_="popular_tags").find_all("a")
        ]
        assert len(tags) >= 1
        tags_str = ", ".join(tags)
    except Exception:
        tags_str = np.nan
    return tags_str


def get_steam_achievements(soup):
    """Get steam achievements from listing page."""
    try:
        ach_div = soup.find(
            "div",
            {"id": "bannerAchievements", "class": "responsive_banner_link"},
        )
        ach_div_span = ach_div.find("span")
        num_steam_achievements = int(
            regex_get_num_from_str((ach_div_span.text))
        )
    except Exception:
        num_steam_achievements = np.nan
    return num_steam_achievements


def get_system_requirements(soup):
    """
    Get system requirements from listing page.

    Notes
    -----
    1. Not used as this is not reliably extracting sysreqs. Needs improvement.
    """
    specs = {}
    for platform in ["win", "mac"]:
        p_soup = soup.find(
            "div", {"class": "game_area_sys_req", "data-os": platform}
        )
        if p_soup:
            min_reqs = soup.find("div", class_="game_area_sys_req_leftCol")
            rec_reqs = soup.find("div", class_="game_area_sys_req_rightCol")
            try:
                specs[f"minimum_{platform}"] = ", ".join(
                    [
                        f"[{min_req.text.strip()}]"
                        for min_req in min_reqs.find_all("li")
                    ]
                )
            except Exception:
                specs[f"minimum_{platform}"] = ""
            try:
                specs[f"recommended_{platform}"] = ", ".join(
                    [
                        f"[{rec_req.text.strip()}]"
                        for rec_req in rec_reqs.find_all("li")
                    ]
                )
            except Exception:
                specs[f"recommended_{platform}"] = ""
        else:
            specs[f"minimum_{platform}"] = ""
            specs[f"recommended_{platform}"] = ""
    return specs


def get_rating(soup):
    """Get game rating from listing page."""
    try:
        rating_main = soup.find("div", class_="shared_game_rating")
        rating_main_all_divs = rating_main.find_all("div")
        # Rating
        rating_url = (
            rating_main_all_divs[0]
            .find("div", class_="game_rating_icon")
            .find("img")["src"]
        )
        rating = os.path.splitext(os.path.basename(rating_url))[0]
        # print(rating)
    except Exception:
        rating = np.nan
    return {"rating": rating}


def get_rating_descriptors(soup):
    """Get descriptive text in game rating from listing page."""
    try:
        rating_main = soup.find("div", class_="shared_game_rating")
        rating_main_all_divs = rating_main.find_all("div")
        # Descriptors
        rating_descriptors = (
            rating_main_all_divs[2:][0]
            .find("div", class_="game_rating_descriptors")
            .find("p")
        )
        rating_descriptors_str = (
            rating_descriptors.text.strip()
            .replace("\r", "")
            .replace("\n", ", ")
        )
    except Exception:
        rating_descriptors_str = np.nan
    return {"rating_descriptors": rating_descriptors_str}


def get_drm(soup):
    """Get DRM/EULA, if any, from listing page."""
    drm_div = soup.find("div", class_="DRM_notice")
    try:
        eula_list = [drm.text.strip() for drm in drm_div.find_all("div")]
        assert len(eula_list) >= 1
        eula_str = ", ".join(eula_list)
    except Exception:
        eula_str = np.nan
    return eula_str


def scrape_game_listing(soup):
    """Scrape a single listing to retrieve various attributes."""
    # Extract info from user reviews summary bar
    num_reviews_int = get_all_reviews_count(soup)
    overall_review_rating = get_overall_review_rating(soup)
    platforms = get_platforms(soup)
    user_defined_tags = get_user_defined_tags(soup)
    num_steam_achievements = get_steam_achievements(soup)
    # system_requirements = get_system_requirements(soup)
    pct_overall, threshold_used = get_pct_overall_review_rating(soup)
    (
        pct_overall_lang,
        threshold_used_lang,
    ) = get_pct_overall_review_rating_language_filtered(soup)
    drm = get_drm(soup)
    listing_info = {
        "review_type_all": num_reviews_int,
        "overall_review_rating": overall_review_rating,
        "pct_overall": pct_overall,
        "pct_overall_threshold": threshold_used,
        "pct_overall_lang": pct_overall_lang,
        "pct_overall_threshold_lang": threshold_used_lang,
        "platforms": platforms,
        "user_defined_tags": user_defined_tags,
        "num_steam_achievements": num_steam_achievements,
        "drm": drm,
    }
    rating_dict = get_rating(soup)
    rating_desc_dict = get_rating_descriptors(soup)
    # listing_info.update(system_requirements)
    listing_info.update(rating_dict)
    listing_info.update(rating_desc_dict)
    listing_info = get_sub_review_counts(soup, listing_info)
    listing_info = get_release_summary_details(soup, listing_info)
    listing_info = get_languages(soup, listing_info)
    return listing_info

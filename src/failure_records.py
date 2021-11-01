#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Handling unexpected failures during extraction of attributes."""


# pylint: disable=invalid-name,broad-except


def dict_failed_extraction_from_search_results():
    """
    Return a dict of Nones for all attributes expected from search results.

    Notes
    -----
    1. Only triggered if error is not caught by exception hadling during
       extraction of attributes from search results page.
    """
    return {
        "page_num": None,
        "app_id_listing": None,
        "url_listing": None,
        "title_listing": None,
        "release_date_listing": None,
        "price_listing": None,
        "sale_listing": None,
        "overall_listing": None,
        "threshold_pct_listing": None,
        "num_reviews_listing": None,
    }


def dict_failed_extraction_from_listing_page():
    """
    Return a dict of Nones for all attributes expected from listing page.

    Notes
    -----
    1. Only triggered if error is not caught by exception hadling during
       extraction of attributes from page for a single listing.
    """
    return {
        "review_type_all": None,
        "overall_review_rating": None,
        "pct_overall": None,
        "pct_overall_threshold": None,
        "pct_overall_lang": None,
        "pct_overall_threshold_lang": None,
        "platforms": None,
        "user_defined_tags": None,
        "num_steam_achievements": None,
        "drm": None,
        "rating": None,
        "rating_descriptors": None,
        "languages": None,
        "num_languages": None,
        "review_type_positive": None,
        "review_type_negative": None,
        "review_language_mine": None,
        "Title": None,
        "Genre": None,
        "Release Date": None,
        "Early Access Release Date": None,
        "Developer": None,
        "Publisher": None,
        "Franchise": None,
    }

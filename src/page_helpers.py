#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Helpers for checking if possible to move forward to next page."""


# pylint: disable=invalid-name,broad-except


import math
import re


def get_pages(pagination, verbose=False):
    """Get current page#, page# of the displayed listings and all pages."""
    # Total listings
    total_listings_element = pagination.find_element_by_xpath(
        './/div[@class="search_pagination_left"]'
    )
    total_listings = int(total_listings_element.text.split()[-1])
    # Maximum page of listings
    max_page_listings = math.ceil(total_listings / 25)
    # All available listings being shown on page
    showing = pagination.find_element_by_xpath(
        './/div[@class="search_pagination_left"]'
    ).text
    showing_listings = list(map(int, re.findall(r"\d+", showing)))[:-1]
    # Current page
    curr_page_list = [
        int(showing_listing / 25) for showing_listing in showing_listings
    ]
    if 0 in curr_page_list:
        current_page_num = 1
    else:
        current_page_num = max(curr_page_list)
    # Get all page numbers (except the current page number)
    all_page_nums = []
    nav_elements = pagination.find_elements_by_xpath(
        './/div[@class="search_pagination_right"]/a'
    )
    for nav_element in nav_elements:
        if nav_element.text not in ["<", ">"]:
            all_page_nums.append(int(nav_element.text))
    all_page_nums = list(
        set(all_page_nums + [current_page_num]) - set([max_page_listings])
    )
    all_page_nums = sorted(all_page_nums)

    if verbose:
        all_page_nums_str = ",".join([str(p) for p in all_page_nums])
        print(
            f"Available page numbers={all_page_nums_str}, "
            f"Current page={current_page_num}, Max page={max(all_page_nums)}"
        )
    return [current_page_num, curr_page_list, all_page_nums]


def check_movement(pagination):
    """Check for ability to navigate backward or forward between pages."""
    pagination_movements = pagination.find_element_by_xpath(
        './/div[@class="search_pagination_right"]'
    ).find_elements_by_class_name("pagebtn")
    # Check for ability to move back
    try:
        move_back_a = pagination_movements[0]
        assert move_back_a.text == "<"
        can_move_back = True
        print("Can move back, ", end="")
    except Exception:
        can_move_back = False
        print("Can not move back, ", end="")

    # Check for ability to move forward
    try:
        move_forward_a = pagination_movements[-1]
        assert move_forward_a.text == ">"
        can_move_forward = True
        print("Can move forward")
    except Exception:
        can_move_forward = False
        print("Can not move forward, ", end="")
    return [can_move_back, can_move_forward]

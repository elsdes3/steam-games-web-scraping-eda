#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Helper functions for navigating a web page with selenium."""

import time
from random import randint, shuffle, uniform

from selenium.webdriver.common.action_chains import ActionChains

from src.selenium_helpers import smooth_scroll_until_element_in_view

# pylint: disable=invalid-name,broad-except


def perform_random_navigation_on_page(
    driver, min_num_hovers=randint(2, 7), max_num_hovers=randint(5, 10)
):
    """Randomly navagate across the Steam store webpage."""
    if min_num_hovers > 5:
        # Smoothly scroll to categories flyout
        categories_flyout = driver.find_element_by_xpath(
            './/div[@data-flyout="genre_flyout"]'
        )
        driver = smooth_scroll_until_element_in_view(driver, categories_flyout)
        time.sleep(uniform(0.8, 1.4))
        # Un-hide categories flyout
        categories_flyout_updated = driver.find_element_by_xpath(
            './/div[@data-flyout="genre_flyout"]'
        )
        categories_flyout_updated.click()
        print("Clicked on categories fly-out")
    else:
        # Mouse over the categories flyout
        actions = ActionChains(driver)
        categories_flyout = driver.find_element_by_xpath(
            './/div[@data-flyout="genre_flyout"]'
        )
        actions.move_to_element(categories_flyout).perform()
        print("Moved the mouse cursor over the categories fly-out")

    # Get all categories' web elements
    categories_menu = driver.find_element_by_xpath(
        './/div[@id="genre_flyout"]/div'
    ).find_elements_by_tag_name("div")
    print("Retrieved raw categories and sub-categories, including blanks")

    # Extract a list of web elements for the Genres
    categories_indexes = [0, 2, 8, 10, 18, 26]
    all_genres = []
    for single_cat in [
        cm for k, cm in enumerate(categories_menu) if k in categories_indexes
    ]:
        single_cat_subsections = single_cat.find_elements_by_tag_name("a")
        for single_cat_subsection in single_cat_subsections:
            # print(q, m, single_cat_subsection.text)
            all_genres.append(single_cat_subsection)
    # Shuffle the list of Genre elements so that order is removed
    shuffle(all_genres)
    print("Retrieved categories and sub-categories with links")

    # Get a (random) number of hovers (to be performed on the page)
    num_sub_cats_to_hover_over = randint(min_num_hovers, max_num_hovers)

    # Perform hovers
    for genre in all_genres[:num_sub_cats_to_hover_over]:
        hover = ActionChains(driver).move_to_element(genre)
        hover.perform()
        time.sleep(uniform(0, 1.8))
    print(f"Performed {num_sub_cats_to_hover_over} hovers on page")

    # Get Install Steam button
    install_steam_button = driver.find_element_by_xpath(
        './/a[@class="header_installsteam_btn_content"]'
    )
    driver = smooth_scroll_until_element_in_view(driver, install_steam_button)
    time.sleep(uniform(0.5, 1.2))
    # Hover over Install Steam button (also collapses opened Categories menu)
    hover = ActionChains(driver).move_to_element(install_steam_button)
    hover.perform()
    print("Hovered over the Install Steam button")
    return driver


def randomly_interact_with_tag_based_filters(
    driver, min_tags_to_filter=2, max_tags_to_filter=6
):
    """Randomly select and unselect various tag-based filters."""
    # Get all tags
    narrow_by_tag = driver.find_element_by_xpath(
        './/div[@data-collapse-name="tags"]'
    )
    tags = narrow_by_tag.find_element_by_xpath(
        './/div[@class="block_content block_content_inner"]/div'
    ).find_elements_by_tag_name("div")

    # Click to filter and un-filter by random tags
    tag_indexes = list(
        range(1, randint(min_tags_to_filter, max_tags_to_filter))
    )
    tag_action_indexes = [tag_indexes, tag_indexes[::-1]]
    for tag_action_index in tag_action_indexes:
        for tag_index in tag_action_index:
            single_tag = (
                tags[tag_index]
                .find_element_by_tag_name("span")
                .find_elements_by_tag_name("span")
            )
            single_tag[0].click()
            time.sleep(uniform(1, 2.2))
    print(f"Selected and Un-selected {len(tag_indexes)} tags")
    return driver


def randomly_interact_with_feature_based_filters(
    driver, min_feats_to_filter=2, max_feats_to_filter=6
):
    """Randomly select and unselect various feature-based filters."""
    # Expand narrow by features header to expand block
    feat_header = driver.find_element_by_xpath(
        './/div[@data-collapse-name="category2"]/div'
    )
    feat_header.click()
    time.sleep(uniform(0.5, 2.2))

    # Get all features
    narrow_by_feat = driver.find_element_by_xpath(
        './/div[@data-collapse-name="category2"]'
    )
    feats = narrow_by_feat.find_element_by_xpath(
        './/div[@class="block_content block_content_inner"]'
    ).find_elements_by_tag_name("div")

    # Click to filter and un-filter by feature
    feat_indexes = list(
        range(1, randint(min_feats_to_filter, max_feats_to_filter))
    )
    feat_action_indexes = [feat_indexes, feat_indexes[::-1]]
    for feat_action_index in feat_action_indexes:
        for feat_index in feat_action_index:
            single_feat = (
                feats[feat_index]
                .find_element_by_tag_name("span")
                .find_elements_by_tag_name("span")
            )
            single_feat[0].click()
            time.sleep(uniform(1, 2.2))
    print(f"Selected and Un-selected {len(feat_indexes)} features")

    # Close narrow by feature expandable block
    feat_header.click()
    return driver

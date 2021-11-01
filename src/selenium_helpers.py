#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Helpers for interacting with elements on a web page with selenium."""


# pylint: disable=invalid-name,broad-except,too-many-arguments


import time
from random import choice, randint, sample, shuffle, uniform

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


def enter_age(driver):
    """Enter a random date of birth for a listing with age restrictions."""
    months_of_the_year = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    try:
        # Enter a random day of the month
        day_xpath = './/select[@id="ageDay"]'
        select = Select(driver.find_element_by_xpath(day_xpath))
        select.select_by_visible_text(f"{str(randint(1, 28+1))}")
        # Enter a random month
        select = Select(
            driver.find_element_by_xpath('.//select[@id="ageMonth"]')
        )
        select.select_by_visible_text(f"{choice(tuple(months_of_the_year))}")
        # Enter a random year
        select = Select(
            driver.find_element_by_xpath('.//select[@id="ageYear"]')
        )
        select.select_by_visible_text(f"{str(randint(1975, 2000))}")
        age_entry = True
        print("COMPLETED AGE CHECK: Age entry required")
    except Exception:
        print("COMPLETED AGE CHECK: Age entry was not required")
        age_entry = False
    # Click proceed button
    proceed_button = driver.find_elements_by_xpath(
        './/div[@class="agegate_text_container btns"]/a'
    )
    proceed_button[0].click()
    return [driver, age_entry]


def sort_search_results(driver):
    """Sort displayed search results."""
    # Get options from the sort dropdown menu
    dropdown_sort = driver.find_element_by_xpath('.//a[@class="trigger"]')
    # Can only click this dropdown once
    dropdown_sort.click()
    time.sleep(uniform(0.9, 2.1))

    # Get dropdown options to sort
    dropdown_sort_options = driver.find_element_by_xpath(
        './/div[@class="dropcontainer"]/ul'
    ).find_elements_by_tag_name("li")

    # Shuffle all dropdown options
    shuffle(dropdown_sort_options)

    # (Randomly) Scroll through all dropdown options
    for sort_option in dropdown_sort_options:
        print(f"Scrolled to sort option: {sort_option.text}")
        hover = ActionChains(driver).move_to_element(sort_option)
        hover.perform()
        time.sleep(uniform(1.1, 2.9))
    return driver


def scroll_up_down_page(
    driver,
    by_how_much=22,
    min_num_pauses=1,
    max_num_pauses=4,
    min_pause=0.1,
    max_pause=2.4,
    scroll_method="slow",
    scroll_direction="up",
):
    """
    Fast or slow scrolling up or down on a page.

    Parameters
    -----
    by_how_much : int
        By how much to scroll (i.e. scroll every 15 to reach end of the page)
    min_num_pauses : int
        Min number of pauses during scrolling
    max_num_pauses : int
        Max number of pauses during scrolling
    min_pause: float
        Minimum duration of pause
    max_pause: float
        Maximum duration of pause
    scroll_method : str
        How to scroll, fast or slow
    scroll_direction : str
        Direction of scrolling, up or down

    Notes
    -----
    1. For no pauses, set min_num_pauses = max_num_pauses.
    """
    # Get total height of page
    total_height = int(
        driver.execute_script("return document.body.scrollHeight")
    )

    if scroll_direction == "down":
        scroll_steps = list(range(1, total_height, by_how_much))
    else:
        scroll_steps = list(range(total_height, 1, -by_how_much))

    if scroll_method == "slow":
        # Scroll in steps
        for i in scroll_steps:
            if max_num_pauses > min_num_pauses:
                # Pause between steps
                stop_points = sample(
                    scroll_steps, randint(min_num_pauses, max_num_pauses)
                )
                if i in stop_points:
                    time.sleep(uniform(min_pause, max_pause))
            driver.execute_script(f"window.scrollTo(0, {i});")
    else:
        # Scroll in one fluid motion, without steps
        if scroll_direction == "down":
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
        else:
            driver.execute_script(
                "window.scrollTo(0, -document.body.scrollHeight);"
            )


def smooth_scroll_until_element_in_view(driver, element):
    """Smoothly scroll up or down until an element is in view."""
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth'});", element
    )
    return driver

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Helper functions for webscraping."""


from random import choice

# pylint: disable=line-too-long


def get_random_user_agent():
    """Return a random user-agent manually extracted from a local browser."""
    ua_dict = {
        "firefox": (
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) "
            "Gecko/20100101 Firefox/93.0"
        ),
        "firefox-private": (
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) "
            "Gecko/20100101 Firefox/93.0"
        ),
        "chrome-incognito": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        ),
        "chrome": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        ),
        "brave-incognito": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
        ),
        "brave": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
        ),
        "edge-beta": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/95.0.4638.32 Safari/537.36 "
            "Edg/95.0.1020.14"
        ),
        "edge-beta-private": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/95.0.4638.32 Safari/537.36 "
            "Edg/95.0.1020.14"
        ),
        "vivaldi": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        ),
        "vivaldi - incognito": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        ),
        "opera - incognito": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
        ),
        "opera": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 "
            "OPR/80.0.4170.16"
        ),
    }
    browser = choice(list(ua_dict.keys()))
    print(f"Selected user-agent from: {browser}")
    return ua_dict[browser]


def get_custom_headers_list():
    """Return list of web request headers taken from local browser."""
    headers_list = [
        # Edge - Windows 8.1
        {
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "sec-ch-ua": (
                '"Chromium";v="94", "Microsoft Edge";v="94", ";'
                'Not A Brand";v="99"'
            ),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/94.0.4606.71 "
                "Safari/537.36 Edg/94.0.992.38"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;"
                "q=0.9"
            ),
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "en-US,en;q=0.9",
        },
        # Edge - Windows 8.1 with Referer = Google
        {
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "sec-ch-ua": (
                '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";'
                'v="99"'
            ),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 "
                "Edg/94.0.992.38"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;"
                "q=0.9"
            ),
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.ca/",
            "Accept-Language": "en-US,en;q=0.9",
        },
        # Firefox - Windows 8.1
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:93.0) Gecko/"
                "20100101 Firefox/93.0"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "avif,image/webp,*/*;q=0.8"
            ),
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "DNT": "1",
        },
        # Firefox - Windows 8.1 with Referer = Google
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:93.0) Gecko/"
                "20100101 Firefox/93.0"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "avif,image/webp,*/*;q=0.8"
            ),
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Referer": "https://www.google.ca/",
            "DNT": "1",
        },
        # Chrome - Windows 8.1 with Referer = Google
        {
            "sec-ch-ua": (
                '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v='
                '"99"'
            ),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
            ),
            "Referer": "https://www.google.ca/",
        },
        # Vivaldi - Windows 8.1 with Referer = Google
        {
            "Connection": "keep-alive",
            "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "avif,image/webp,image/apng,*/*;q=0.8,application/signed-"
                "exchange;v=b3;q=0.9"
            ),
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.ca/",
            "Accept-Language": "en-US,en;q=0.9",
        },
        # Opera - Windows 8.1 with Referer = Google
        {
            "Connection": "keep-alive",
            "sec-ch-ua": (
                '"Chromium";v="94", " Not A;Brand";v="99", "Opera";v="80"'
            ),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/"
                "80.0.4170.40"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "avif,image/webp,image/apng,*/*;q=0.8,application/signed-"
                "exchange;v=b3;q=0.9"
            ),
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.ca/",
            "Accept-Language": "en-US,en;q=0.9",
        },
        # Brave - Windows 8.1 with Referer = Google
        {
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "avif,image/webp,image/apng,*/*;q=0.8,application/signed-"
                "exchange;v=b3;q=0.9"
            ),
            "Sec-GPC": "1",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.ca/",
            "Accept-Language": "en-US,en;q=0.9",
        },
        # Firefox Linux with no Referer
        {
            "User-Agent": (
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/"
                "20100101 Firefox/93.0"
            ),
            "Accept": "image/avif,image/webp,*/*",
            "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "image",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-origin",
        },
        # Firefox Linux with Referer = Google
        {
            "User-Agent": (
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/"
                "20100101 Firefox/93.0"
            ),
            "Accept": "image/avif,image/webp,*/*",
            "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
            "Connection": "keep-alive",
            "Referer": "https://www.google.com/",
            "Sec-Fetch-Dest": "image",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-origin",
        },
        # Chrome Linux with no Referer
        {
            "sec-ch-ua": (
                '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";'
                'v="99"'
            ),
            "Accept": "*/*",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                "like Gecko) Chrome/94.0.4606.81 Safari/537.36"
            ),
            "sec-ch-ua-platform": '"Linux"',
        },
        # Chrome Linux with Referer = Google
        {
            "sec-ch-ua": (
                '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v='
                '"99"'
            ),
            "Accept": "*/*",
            "Referer": "https://www.google.com/",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                "like Gecko) Chrome/94.0.4606.81 Safari/537.36"
            ),
            "sec-ch-ua-platform": '"Linux"',
        },
        # Brave with no Referer
        {
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                "like Gecko) Chrome/94.0.4606.81 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "avif,image/webp,image/apng,*/*;q=0.8,application/signed-"
                "exchange;v=b3;q=0.9"
            ),
            "Sec-GPC": "1",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        },
        # Brave Linux with Referer = Google
        {
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                "like Gecko) Chrome/94.0.4606.81 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "avif,image/webp,image/apng,*/*;q=0.8,application/signed-"
                "exchange;v=b3;q=0.9"
            ),
            "Sec-GPC": "1",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        },
        # Opera Linux with no Referer
        {
            "Connection": "keep-alive",
            "sec-ch-ua": (
                '"Chromium";v="94", " Not A;Brand";v="99", "Opera";v="80"'
            ),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                "like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/80.0.4170."
                "40"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "avif,image/webp,image/apng,*/*;q=0.8,application/signed-"
                "exchange;v=b3;q=0.9"
            ),
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "en-US,en;q=0.9",
        },
        # Opera Linux with Referer = Google
        {
            "Connection": "keep-alive",
            "sec-ch-ua": (
                '"Chromium";v="94", " Not A;Brand";v="99", "Opera";v="80"'
            ),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                "like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/80.0.4170."
                "40"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "avif,image/webp,image/apng,*/*;q=0.8,application/signed-"
                "exchange;v=b3;q=0.9"
            ),
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Language": "en-US,en;q=0.9",
        },
        # Edge Linux with no Referer
        {
            "Connection": "keep-alive",
            "sec-ch-ua": (
                '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";'
                'v="99"'
            ),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                "like Gecko) Chrome/95.0.4638.40 Safari/537.36 Edg/95.0.1020."
                "20"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q"
                "=0.9"
            ),
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
        },
        # Edge Linux with Referer = Google
        {
            "Connection": "keep-alive",
            "sec-ch-ua": (
                '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v'
                '="99"'
            ),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                "like Gecko) Chrome/95.0.4638.40 Safari/537.36 Edg/95.0.1020."
                "20"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q"
                "=0.9"
            ),
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
        },
        # Vivaldi Linux with no Referer
        {
            "Connection": "keep-alive",
            "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                "like Gecko) Chrome/94.0.4606.81 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "avif,image/webp,image/apng,*/*;q=0.8,application/signed-"
                "exchange;v=b3;q=0.9"
            ),
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        },
        # Vivaldi Linux with Referer = Google
        {
            "Connection": "keep-alive",
            "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                "like Gecko) Chrome/94.0.4606.81 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "avif,image/webp,image/apng,*/*;q=0.8,application/signed-"
                "exchange;v=b3;q=0.9"
            ),
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        },
        # Firefox 77 Mac
        {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) "
                "Gecko/20100101 Firefox/77.0"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "webp,*/*;q=0.8"
            ),
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        },
        # Firefox 77 Windows
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/"
                "20100101 Firefox/77.0"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "webp,*/*;q=0.8"
            ),
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        },
        # Chrome 83 Mac
        {
            "Connection": "keep-alive",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/"
                "537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;"
                "q=0.9"
            ),
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        },
        # Chrome 83 Windows
        {
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                "webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;"
                "q=0.9"
            ),
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
        },
    ]
    return headers_list

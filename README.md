# Web Scraping & Exploratory Analysis for PC Game listings on the Steam web store

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/elsdes3/steam-games-web-scraping-eda)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/elsdes3/steam-games-web-scraping-eda/master/0_get_agg_data.ipynb)
![CI](https://github.com/elsdes3/steam-games-web-scraping-eda/workflows/CI/badge.svg)
![CodeQL](https://github.com/elsdes3/steam-games-web-scraping-eda/actions/workflows/codeql-analysis.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/mit)
![OpenSource](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![prs-welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)
![pyup](https://pyup.io/repos/github/elsdes3/steam-games-web-scraping-eda/shield.svg)

## [Table of Contents](#table-of-contents)
1. [About](#about)
   * [Brief Background](#brief-background)
   * [Objectives](#objectives)
   * [Analysis](#analysis)
2. [Pre-Requisites](#pre-requisites)
3. [Notebooks](#notebooks)
4. [Notes](#notes)
5. [Project Organization](#project-organization)

## [About](#about)

Webscraping and exploratory data analysis of PC game listings with Python.

### [Brief Background](#brief-background)
The video game industry is involved in the development, marketing, and distribution of video games. All games require a platform or system on which they operate. This project focuses on games that run on a PC. Digital distribution platforms have assumed control over a large section of the PC gaming market. The Bigest digital distributor is [Steam](https://store.steampowered.com/about/), developed by [Valve](https://www.valvesoftware.com/en/about) in 2003 to manage upgrades for its own games. Currently, Steam offers a webstore to primarily purchase games. It also offers a fully online social community for gamers and PC game developers.

### [Objectives](#objectives)
The primary motivation for this project is to gather data about how the developer and the customer (end-users, or gamers) communicate/interact with the Steam platform. For developers, the specific interest is in analyzing their presence on the platform: how many games do they offer, what does Steam offer them, what technical obstacles do they experience? A secondary objective is to analyze user interaction with the Steam web store in order to purchase a game.

### [Analysis](#analysis)
High-level exploratory analysis will be performed in this project, by scraping data about the game listings and some attributes of user reviews (for each listing) on the Steam web store.

## [Pre-Requisites](#pre-requisites)
1. Export the following environment variables (required for interacting with Azure blob storage, where scraped data will be stored) and a MySQL database (where scraped and cleaned data will be stored)
   ```bash
   # Azure Blob Storage
   export BLOB_NAME_PREFIX=<value-here>
   export AZURE_STORAGE_KEY=<credential-here>
   export ENDPOINT_SUFFIX=<value-here>
   export AZURE_STORAGE_ACCOUNT=<credential-here>
   # MySQL
   export MYSQL_ADMIN_USER_NAME=<credential-here>
   export MYSQL_ADMIN_USER_PWD=<credential-here>
   export MYSQL_NON_ADMIN_USER_NAME=<credential-here>
   export MYSQL_NON_ADMIN_USER_PWD=<credential-here>
   export MYSQL_HOST=localhost
   export MYSQL_PORT=3306
   ```
2. Run the notebooks that do not require web-scraping
   ```bash
   make build
   ```

## [Notebooks](#notebooks)
1. `0_get_agg_data.ipynb` ([view](https://nbviewer.jupyter.org/github/elsdes3/steam-games-web-scraping-eda/blob/main/0_get_agg_data.ipynb))
   - scrape aggregated data about PC game listings from search function of Steam web store
2. `1_eda_aggregated.ipynb`([view](https://nbviewer.jupyter.org/github/elsdes3/steam-games-web-scraping-eda/blob/main/1_eda_aggregated.ipynb))
   - explore aggregated data in order to determine whether reasonable filters can be applied to reduce the number of listings that will be scraped
3. `2_selenium.ipynb` (used for web scraping first 49 pages of search results with Selenium) ([view](https://nbviewer.jupyter.org/github/elsdes3/steam-games-web-scraping-eda/blob/main/2_selenium.ipynb))
   - specify single page number of search results to be scraped
   - navigate to search page (with `?page=1` in URL)
   - click on *Games* to filter search results to only include games
   - navigate to the page number (specified above) to be scraped (clicking the forward button in the page navigation pane at the bottom of the search listings)
   - scrape full page of 25 search results
   - create pandas `DataFrame` with these 25 rows
   - export pandas `DataFrame` to `.parquet.gzip` file
   - click on first search result to go to its listing page
   - scrape listing
   - export scraped listing's attributes to a single-row CSV file
   - move back to search results page
   - click on second search result ...
   - repeat for all 25 search results
   - close the browser

   There are pauses, random hovers and random mouse movements at various points in the scraping. See the notebook for details.

   This notebook only supports scraping a single page of search results at a time. It should be run manually by changing the page-number Python variable to the search results page number to be scraped.
4. `3_requests_download.ipynb` (scrapes a range of search results pages with `requests`; used to scrape the next few hundred pages of search results starting from page 50) ([view](https://nbviewer.jupyter.org/github/elsdes3/steam-games-web-scraping-eda/blob/main/3_requests_download.ipynb))
   - send `GET` request to search results page
   - scrape all 25 search results on page
   - create pandas `DataFrame` with these 25 rows
   - export pandas `DataFrame` to `.parquet.gzip` file
   - check if possible to load the next page number and, if possible, load the next page of search results
   - scrape all 25 ...
   - repeat for all pages of search results in the range of search results pages (specified above) to be scraped

   There is a single pause between scraping successive listings.
5. `4_filter_requests_listings.ipynb` ([view](https://nbviewer.jupyter.org/github/elsdes3/steam-games-web-scraping-eda/blob/main/4_filter_requests_listings.ipynb))
   - remove duplicate listings from *search results* dataset scraped with `requests`
     - after this, each row refers to a unique listing to be scraped
   - export processed dataset to CSV file
6. `5_requests_listings_download.ipynb` ([view](https://nbviewer.jupyter.org/github/elsdes3/steam-games-web-scraping-eda/blob/main/5_requests_listings_download.ipynb))
   - use `requests` to scrape all rows (listings) of *search results* dataset with no duplicates
   - export each scraped listing's attributes to a single-row CSV
7. `6_merge_searches_listings.ipynb` ([view](https://nbviewer.jupyter.org/github/elsdes3/steam-games-web-scraping-eda/blob/main/6_merge_searches_listings.ipynb))
   - create the *listings* dataset
     - concatenate all single-row CSVs of scraped listing attributes from into pandas `DataFrame` to create the *listings* dataset
     - process (remove duplicates, handle missing values and rows that refer to more than a single game)
   - merge with *search results* dataset
   - perform this separately with data scraped using `selenium` and `requests`
   - combine merged datasets for `selenium` and `requests` and save to disk
8. `7_eda_v2.ipynb` ([view](https://nbviewer.jupyter.org/github/elsdes3/steam-games-web-scraping-eda/blob/main/7_eda_v2.ipynb))
   - exploratory data analysis
9. `8_upload_cloud.ipynb`([view](https://nbviewer.jupyter.org/github/elsdes3/steam-games-web-scraping-eda/blob/main/8_upload_cloud.ipynb))
   - upload scraped data to presonal (private) cloud storage
10. `9_download_cloud.ipynb`([view](https://nbviewer.jupyter.org/github/elsdes3/steam-games-web-scraping-eda/blob/main/9_download_cloud.ipynb))
    - download scraped data from presonal (private) cloud storage
11. `10_selenium_to_db.ipynb`([view](https://nbviewer.jupyter.org/github/elsdes3/steam-games-web-scraping-eda/blob/main/10_selenium_to_db.ipynb))
    - ETL to retrieve and clean raw data scraped with Selenium (from cloud storage) and append to a MySQL database

## [Notes](#notes)
1. Web-scraping was started using the Selenium package and this was used to scrape approximately 50 pages of search results. However, due to very slow scraping speeds, the `requests` library was used to scrape the next few hundred pages of search results.
2. The following workflow was followed for webscraping in this project
   - perform a search for *Game* listings on the [Steam web store](https://store.steampowered.com/)
     - to do this, the search filter `?page=1` needs to be in the URL in order to access the pages of search results (with 25 search results displayed per page) instead of an infinite scrolling single page with results
     - this dataset is first scraped and is referred to as the *search results* dataset (a pandas `DataFrame` is created to hold these results)
     - each row of this dataset (or, each search result) is a single game listing that will be scraped next
     - since the search results were scraped over several days, the listings displayed on the same search results page number changed from one scrape of this dataset to the next as more listings were added to the webstore; this caused previously scraped listings to be moved to a later page (for example, they might have been moved from page 4 of the search results to page 7) resulting in duplication of listings across multiple pages of search results
   - for every row in the *search results* dataset, the game listing in the URL column is then scraped and a single row CSV file is produced for each listing
     - this dataset is referred to as the *listings* dataset
     - to avoid scraping the same listing multiple times, the Python code implemented here will either check if a CSV file of the required listing name already exists (scraping with `selenium`) or call `.drop_duplicates()` on the *search results* `DataFrame` before scraping the unique listing on each row (scraping with `requests`)
       - in either case, the same listing is not scraped multiple times
   - all single-row CSVs are vertically concatenated to give a final *listings dataset* which is then merged with the *search results dataset* and used for exploratory data analysis

## [Project Organization](#project-organization)

    ├── LICENSE
    ├── .env                          <- environment variables (verify this is in .gitignore)
    ├── .gitignore                    <- files and folders to be ignored by version control system
    ├── .pre-commit-config.yaml       <- configuration file for pre-commit hooks
    ├── .github
    │   ├── workflows
    │       └── main.yml              <- configuration file for CI build on Github Actions
    ├── Makefile                      <- Makefile with commands like `make lint` or `make build`
    ├── README.md                     <- The top-level README for developers using this project.
    ├── environment.yml               <- configuration file to create environment to run project on Binder
    ├── data
    │   ├── raw                       <- Scripts to download or generate data
    |   └── processed                 <- merged and filtered data, sampled at daily frequency
    ├── *.ipynb                       <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                                    and a short `-` delimited description, e.g. `1.0-jqp-initial-data-exploration`.
    ├── requirements.txt              <- base packages required to execute all Jupyter notebooks (incl. jupyter)
    ├── src                           <- Source code for use in this project.
    │   ├── __init__.py               <- Makes src a Python module
    │   └── *.py                      <- Scripts to use in analysis for pre-processing, visualization, training, etc.
    ├── papermill_runner.py           <- Python functions that execute system shell commands.
    └── tox.ini                       <- tox file with settings for running tox; see https://tox.readthedocs.io/en/latest/

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

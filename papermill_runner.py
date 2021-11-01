#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Programmatic execution of notebooks."""

# pylint: disable=invalid-name

import os
from datetime import datetime
from typing import Dict, List

import papermill as pm

PROJ_ROOT_DIR = os.getcwd()
data_dir = os.path.join(PROJ_ROOT_DIR, "data")
output_notebook_dir = os.path.join(PROJ_ROOT_DIR, "executed_notebooks")

raw_data_path = os.path.join(data_dir, "raw")

ssl_cert_url = (
    "https://www.digicert.com/CACerts/BaltimoreCyberTrustRoot.crt.pem"
)

six_dict_nb_name = "6_merge_searches_listings.ipynb"
seven_dict_nb_name = "7_eda_v2.ipynb"
nine_dict_nb_name = "9_download_cloud.ipynb"
ten_dict_nb_name = "10_selenium_to_db.ipynb"

six_dict = dict(proc_data_filename="processed_data.csv")
seven_dict = dict(proc_data_filename="processed_data.csv")
nine_dict = dict(
    blob_name_suffixes={
        "listings": 80,
        "search_results": 81,
        "listings_requests": 82,
        "search_results_requests": 83,
    },
)
ten_dict = dict(
    database_name="mydbdemo",
    ssl_cert_url=ssl_cert_url,
    is_database_exists=False,
    is_user_exists=False,
    table_name="listings",
    drop_table=True,
)


def papermill_run_notebook(
    nb_dict: Dict, output_notebook_directory: str = "executed_notebooks"
) -> None:
    """Execute notebook with papermill"""
    for notebook, nb_params in nb_dict.items():
        now = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_nb = os.path.basename(notebook).replace(
            ".ipynb", f"-{now}.ipynb"
        )
        print(
            f"\nInput notebook path: {notebook}",
            f"Output notebook path: {output_notebook_directory}/{output_nb} ",
            sep="\n",
        )
        for key, val in nb_params.items():
            print(key, val, sep=": ")
        pm.execute_notebook(
            input_path=notebook,
            output_path=f"{output_notebook_directory}/{output_nb}",
            parameters=nb_params,
        )


def run_notebooks(
    notebooks_list: List, output_notebook_directory: str = "executed_notebooks"
) -> None:
    """Execute notebooks from CLI.
    Parameters
    ----------
    nb_dict : List
        list of notebooks to be executed
    Usage
    -----
    > import os
    > PROJ_ROOT_DIR = os.path.abspath(os.getcwd())
    > one_dict_nb_name = "a.ipynb
    > one_dict = {"a": 1}
    > run_notebook(
          notebook_list=[
              {os.path.join(PROJ_ROOT_DIR, one_dict_nb_name): one_dict}
          ]
      )
    """
    for nb in notebooks_list:
        papermill_run_notebook(
            nb_dict=nb, output_notebook_directory=output_notebook_directory
        )


if __name__ == "__main__":
    nb_dict_list = [
        nine_dict,
        six_dict,
        seven_dict,
        ten_dict,
    ]
    nb_name_list = [
        nine_dict_nb_name,
        six_dict_nb_name,
        seven_dict_nb_name,
        ten_dict_nb_name,
    ]
    notebook_list = [
        {os.path.join(PROJ_ROOT_DIR, nb_name): nb_dict}
        for nb_dict, nb_name in zip(nb_dict_list, nb_name_list)
    ]
    run_notebooks(
        notebooks_list=notebook_list,
        output_notebook_directory=output_notebook_dir,
    )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Utility functions for notebooks and standalone scripts."""


import os
import re

from IPython.display import display

# pylint: disable=invalid-name


def show_df(df, nrows=None):
    """Show a few of the first and last rows of a DataFrame."""
    df_slice = df.head(nrows).append(df.tail(nrows)) if nrows else df
    header = f"First & Last {nrows} rows" if nrows else "All rows"
    display(df_slice.style.set_caption(header))


def show_df_dtypes_nans(df):
    """Show datatypes and number of missing rows in DataFrame."""
    display(
        df.isna()
        .sum()
        .rename("num_missing")
        .to_frame()
        .merge(
            df.dtypes.rename("dtype").to_frame(),
            left_index=True,
            right_index=True,
            how="left",
        )
        .style.set_caption("Column Datatypes and Missing Values")
    )


def save_to_parquet_file(dfs, parquet_filepaths):
    """Save DataFrame to parquet file."""
    for parquet_filepath, df in zip(parquet_filepaths, dfs):
        try:
            print(f"Saving data to {parquet_filepath + '.gzip'}", end="...")
            df.to_parquet(
                parquet_filepath + ".gzip",
                engine="auto",
                index=False,
                compression="gzip",
            )
            print("done.")
        except Exception as e:
            print(str(e))
            raise


def regex_get_num_from_str(str_obj):
    """Regex to extract number from a string."""
    return re.sub(r"\D", "", str_obj).replace(",", "")


def export_to_csv(df, data_dir, fname_no_ext):
    """Export DataFrame to csv file."""
    listing_filepath = os.path.join(data_dir, f"{fname_no_ext}.csv")
    if not os.path.exists(listing_filepath):
        df.to_csv(listing_filepath, index=False)
        print(f"Exported {fname_no_ext} to CSV file")
    else:
        print(f"Found CSV file for {fname_no_ext}. Did nothing.")

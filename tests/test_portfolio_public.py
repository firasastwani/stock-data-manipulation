"""
Public tests – can be run locally via `pytest -q`.

The auto grader’s *private* test suite will be more exhaustive but will rely
on the same public API.
"""
from datetime import datetime

import pandas as pd
import pytest

from get_portfolio import (
    read_stock_data,
    symbol_to_path,
    get_portfolio_join,
    get_portfolio_concat,
    get_portfolio_merge,
    random_subset,
    random_end_date,
)

# ---------------------------------------------------------------------
# Fixtures/helpers
# ---------------------------------------------------------------------
@pytest.fixture(scope="module")
def google_df():
    return read_stock_data("GOOG")


# ---------------------------------------------------------------------
# read_stock_data basics
# ---------------------------------------------------------------------
def test_symbol_to_path():
    assert symbol_to_path("AAPL").endswith("data/AAPL.csv")


def test_read_stock_data_shape(google_df):
    # file contains multiple years but we just check a couple of rows
    assert google_df.shape[1] == 1          # single column
    assert list(google_df.columns) == ["GOOG"]


def test_read_stock_data_sample(google_df):
    # 2020-03-31 Adj Close value from the provided CSV
    assert abs(google_df.loc["2020-03-31"]["GOOG"] - 58.074413) < 1e-6


# ---------------------------------------------------------------------
# Portfolio builders
# ---------------------------------------------------------------------
SYMS = ["GOOG", "AAPL"]
DATES = pd.date_range("2020-03-31", "2020-04-03")


@pytest.mark.parametrize("builder", [get_portfolio_join,
                                     get_portfolio_concat,
                                     get_portfolio_merge])
def test_portfolio_builders(builder):
    df = builder(SYMS, DATES)
    # shape: 4 trading days × 2 symbols
    assert df.shape == (len(DATES), len(SYMS))
    # value spot-check
    assert abs(df.loc["2020-04-01", "GOOG"] - 55.218162) < 1e-6


# ---------------------------------------------------------------------
# Random utilities
# ---------------------------------------------------------------------
BIG_LIST = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA", "NVDA", "XOM"]

def test_random_subset_deterministic():
    s1 = random_subset(BIG_LIST, k=3, seed=42)
    s2 = random_subset(BIG_LIST, k=3, seed=42)
    assert s1 == s2 and len(s1) == 3


def test_random_end_date():
    new_end, delta = random_end_date("2020-08-01", seed=0)
    assert 3 <= delta <= 14
    assert new_end == datetime(2020, 8, 11)  # seed 0 → delta 10
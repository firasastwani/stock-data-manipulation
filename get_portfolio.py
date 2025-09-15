"""
CSCI 4170/6170 – HW02

Utility functions for building small stock portfolios *using only the CSV
files already present in the local `data/` directory*.

Nothing here touches the network, so the module is safe for an
offline/CI-based auto-grader.

Public API (imported by the tests)
----------------------------------
symbol_to_path(symbol[, base_dir])
read_stock_data(symbol)
get_portfolio_join(symbols, dates[, how])
get_portfolio_concat(symbols, dates[, axis, join])
get_portfolio_merge(symbols, dates[, how])
random_subset(symbols, k[, seed])
random_end_date(start_date[, min_days, max_days, seed])
compute_daily_returns(portfolio_df)
compute_cumulative_returns(portfolio_df)
top_bottom_tickers(cum_returns[, n])
rolling_volatility(portfolio_df[, window])
"""
from __future__ import annotations

import os
import random
from datetime import datetime, timedelta
from typing import Iterable, List, Tuple

import pandas as pd

DATA_DIR = "data"             # folder with all S&P-500 CSVs
_DEFAULT_NA = ["nan"]         # NA strings used in the CSVs
HOW_VALUES = {"left", "right", "inner", "outer"}

__all__ = [
    "symbol_to_path",
    "read_stock_data",
    "get_portfolio_join",
    "get_portfolio_concat",
    "get_portfolio_merge",
    "random_subset",
    "random_end_date",
    "compute_daily_returns",
    "compute_cumulative_returns",
    "top_bottom_tickers",
    "rolling_volatility",
]

# ---------------------------------------------------------------------
# I/O helpers (keep these fully implemented)
# ---------------------------------------------------------------------
def symbol_to_path(symbol: str, base_dir: str = DATA_DIR) -> str:
    """
    Return `<base_dir>/<symbol>.csv` (no existence check here – caller is
    responsible for ensuring the file is present.
    """
    return os.path.join(base_dir, f"{symbol}.csv")


def read_stock_data(symbol: str) -> pd.DataFrame:
    """
    Read one ticker's CSV and return a *single-column* DataFrame whose
    index is the `Date` and whose column name is *the symbol*.

    Raises FileNotFoundError if the CSV is missing – the caller can catch
    this if desired.
    """
    fp = symbol_to_path(symbol)
    df = pd.read_csv(
        fp,
        index_col="Date",
        parse_dates=True,
        usecols=["Date", "Adj Close"],
        na_values=_DEFAULT_NA,
    )
    df.rename(columns={"Adj Close": symbol}, inplace=True)
    return df


# ---------------------------------------------------------------------
# Internal utility (fully implemented)
# ---------------------------------------------------------------------
def _empty_df(dates: pd.DatetimeIndex) -> pd.DataFrame:
    """
    Build an empty DataFrame whose index is a DatetimeIndex aligned to `dates`.
    """
    idx = pd.to_datetime(dates)
    df = pd.DataFrame(index=idx)
    df.index.name = "Date"
    return df


# ---------------------------------------------------------------------
# Portfolio builders (TODO: must implement these)
# ---------------------------------------------------------------------
def get_portfolio_join(
    symbols: Iterable[str],
    dates: pd.DatetimeIndex,
    *,
    how: str = "left",
) -> pd.DataFrame:
    """
    Build a combined DataFrame using successive `DataFrame.join()`.

    TODO: Starting with an empty DataFrame indexed by `dates`,
    iteratively join each symbol's DataFrame using the specified join type (`how`).
    """

    if how not in HOW_VALUES:
        raise ValueError(f"how must be one of {sorted(HOW_VALUES)}")
    # Placeholder behaviour: explain the missing implementation and return an empty DataFrame

    df_res = pd.DataFrame(index=dates)

    for symbol in symbols: 
        cur_df = read_stock_data(symbol)
        df_res = df_res.join(cur_df, how= how)


    return df_res


def get_portfolio_concat(
    symbols: Iterable[str],
    dates: pd.DatetimeIndex,
    *,
    axis: int = 1,
    join: str = "outer",
) -> pd.DataFrame:
    """
    Build a combined DataFrame using `pd.concat`.

    TODO: Use `pd.concat` to combine the list of symbol DataFrames along the
    specified axis, then reindex to `dates` so the final DataFrame has the same index.
    """
    symbol_dfs = []
    for symbol in symbols:
        symbol_df = read_stock_data(symbol)
        symbol_dfs.append(symbol_df)
    
    combined_df = pd.concat(symbol_dfs, axis=axis, join=join)
    
    result_df = combined_df.reindex(dates)
    
    return result_df


def get_portfolio_merge(
    symbols: Iterable[str],
    dates: pd.DatetimeIndex,
    *,
    how: str = "left",
) -> pd.DataFrame:
    """
    Build a combined DataFrame using successive `DataFrame.merge()`.

    TODO: Starting with an empty DataFrame indexed by `dates`,
    iteratively merge each symbol's DataFrame using the specified merge type (`how`).
    """
    if how not in HOW_VALUES:
        raise ValueError(f"how must be one of {sorted(HOW_VALUES)}")
    
    # empty DataFrame indexed by dates
    df_res = pd.DataFrame(index=dates)
    
    # Iteratively merge each symbol's DataFrame
    for symbol in symbols:
        cur_df = read_stock_data(symbol)

        df_res = df_res.merge(cur_df, left_index=True, right_index=True, how=how)
    
    return df_res

    


def random_subset(
    symbols: List[str],
    k: int = 5,
    *,
    seed: int | None = None,
) -> List[str]:
    """
    Return *k* distinct symbols chosen without replacement.

    TODO: Use `random.Random(seed)` and `sample` to select `k` symbols.
    """
    
    # Create a Random instance with the given seed
    rng = random.Random(seed)
    
    # Use sample to select k distinct symbols without replacement
    return rng.sample(symbols, min(k, len(symbols)))

def random_end_date(
    start_date: str | datetime,
    *,
    min_days: int = 3,
    max_days: int = 14,
    seed: int | None = None,
) -> Tuple[datetime, int]:
    """
    Return a tuple `(new_end_date, delta_days)` where `delta_days` is
    chosen uniformly at random in [min_days, max_days] inclusive.

    TODO: Parse `start_date` if necessary, generate a random delta, and return both.
    """
    
    if isinstance(start_date, str):
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    else:
        start_dt = start_date
    
    # Create a Random instance with the given seed
    rng = random.Random(seed)
    
    delta_days = rng.randint(min_days, max_days)
    
    # Calculate end date
    end_dt = start_dt + timedelta(days=delta_days)
    
    return (end_dt, delta_days)
    
    
    
def compute_daily_returns(portfolio_df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute daily percentage returns for each column in the portfolio DataFrame.

    TODO: Use DataFrame.pct_change(fill_method=None) and drop the first row.
    """

    # Calculate percentage change for each column
    pct_change = portfolio_df.pct_change(fill_method=None)
    
    # Drop the first row (which will be NaN since there's no previous value)
    daily_returns = pct_change.dropna()
    
    return daily_returns

def compute_cumulative_returns(portfolio_df: pd.DataFrame) -> pd.Series:
    """
    Compute cumulative returns for each column over the full date range.

    TODO: Multiply (1 + daily returns) across the date range and subtract 1.
    """
    # First compute daily returns
    daily_returns = compute_daily_returns(portfolio_df)
    
    # Calculate cumulative returns: multiply (1 + daily returns) across the date range
    cumulative_growth = (1 + daily_returns).prod()
    
    # Subtract 1 to get the cumulative return percentage
    cumulative_returns = cumulative_growth - 1
    
    return cumulative_returns

def top_bottom_tickers(cum_returns: pd.Series, n: int = 3) -> Tuple[List[str], List[str]]:
    """
    Return two lists: the top `n` and bottom `n` tickers by cumulative return.

    TODO: Sort the Series and take the first `n` and last `n` indices.
    """
    # Sort the Series in descending order (highest returns first)
    sorted_returns = cum_returns.sort_values(ascending=False)
    
    # Get the top n tickers (highest returns)
    top_tickers = sorted_returns.head(n).index.tolist()
    
    #Get the bottom n tickers (lowest returns)
    bottom_tickers = sorted_returns.tail(n).index.tolist()
    
    return (top_tickers, bottom_tickers)

def rolling_volatility(portfolio_df: pd.DataFrame, window: int = 5) -> pd.DataFrame:
    """
    Compute a rolling standard deviation of daily returns.

    TODO: Calculate daily returns first, then use .rolling(window).std().
    """
    # Calculate daily returns first
    daily_returns = compute_daily_returns(portfolio_df)
    
    # Compute rolling standard deviation (volatility) for each column
    rolling_vol = daily_returns.rolling(window=window).std()
    
    return rolling_vol

# ---------------------------------------------------------------------
# Manual demo (optional – remove or comment out)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Example usage: build a portfolio and compute returns.
    # Note: These examples will fail until you implement the functions above.
    start, end = "2020-03-31", "2020-07-29"
    symbols_list = ["GOOG", "AAPL", "XOM", "AMZN", "GLD"]
    dates = pd.date_range(start, end)

    portfolio = get_portfolio_join(symbols_list, dates)
    daily_ret = compute_daily_returns(portfolio)
    cum_ret = compute_cumulative_returns(portfolio)
    top, bottom = top_bottom_tickers(cum_ret, n=3)

    print("Portfolio (head):\n", portfolio.head())
    print("\nDaily Returns (head):\n", daily_ret.head())
    print("\nCumulative Returns:\n", cum_ret)
    print(f"\nTop 3 tickers: {top}")
    print(f"Bottom 3 tickers: {bottom}")

    rolling_vol = rolling_volatility(portfolio, window=20)
    print("\n20‑Day Rolling Volatility (tail):\n", rolling_vol.tail())
    print("\n20‑Day Rolling Volatility (first non‑NaN rows):\n", rolling_vol.dropna().head())

    
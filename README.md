# Portfolio Analysis Project

A comprehensive Python project for building and analyzing stock portfolios using pandas, with support for multiple portfolio construction methods and financial analysis tools.

## 📋 Project Overview

This project provides utilities for building small stock portfolios using CSV data files and performing various financial analyses including daily returns, cumulative returns, volatility analysis, and performance ranking.

## 🚀 Features

- **Multiple Portfolio Construction Methods**:

  - `get_portfolio_join()` - Using DataFrame.join()
  - `get_portfolio_merge()` - Using DataFrame.merge()
  - `get_portfolio_concat()` - Using pd.concat()

- **Financial Analysis Tools**:

  - Daily returns calculation using `pct_change()`
  - Cumulative returns computation
  - Rolling volatility analysis
  - Top/bottom performer identification
  - Random portfolio subset generation

- **Data Management**:
  - CSV data reading and processing
  - Date range generation with random end dates
  - Missing data handling

## 📁 Project Structure

```
Wk03c-HW02-portfolio/
├── data/                           # Stock data CSV files
│   ├── AAPL.csv
│   ├── AMZN.csv
│   ├── CVNA.csv
│   ├── GLD.csv
│   ├── GOOG.csv
│   ├── IBM.csv
│   ├── SPY.csv
│   ├── W.csv
│   └── XOM.csv
├── tests/                          # Test files
│   └── test_portfolio_public.py
├── get_portfolio.py                # Main portfolio utilities
├── get_daily_rate.py              # Daily rate utilities
├── mainTests.py                   # Test runner
├── task03.py                      # Task 3: Portfolio construction methods
├── task04.py                      # Task 4: Portfolio analysis
├── task01a.csv                    # Task 1a results
├── task01b.csv                    # Task 1b results
├── task03a_join.csv               # Task 3a: Join method results
├── task03b_merge.csv              # Task 3b: Merge method results
├── task03c_concat.csv             # Task 3c: Concat method results
├── task04_daily_returns.csv       # Task 4: Daily returns
├── task04_cum_returns.csv         # Task 4: Cumulative returns
├── task04_rolling_volatility_5day.csv # Task 4: Rolling volatility
└── README.md                      # This file
```

## 🛠️ Installation

1. **Clone or download the project**
2. **Set up virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install pandas numpy
   ```

## 📊 Usage

### Basic Portfolio Construction

```python
from get_portfolio import get_portfolio_join, get_portfolio_merge, get_portfolio_concat
import pandas as pd

# Define symbols and date range
symbols = ['AAPL', 'GOOG', 'XOM', 'IBM', 'W']
dates = pd.date_range('2020-08-01', '2020-08-14', freq='D')

# Build portfolio using different methods
portfolio_join = get_portfolio_join(symbols, dates, how='left')
portfolio_merge = get_portfolio_merge(symbols, dates, how='left')
portfolio_concat = get_portfolio_concat(symbols, dates, axis=1, join='outer')
```

### Financial Analysis

```python
from get_portfolio import (
    compute_daily_returns,
    compute_cumulative_returns,
    top_bottom_tickers,
    rolling_volatility
)

# Calculate daily returns
daily_returns = compute_daily_returns(portfolio)

# Calculate cumulative returns
cumulative_returns = compute_cumulative_returns(portfolio)

# Find top and bottom performers
top_performers, bottom_performers = top_bottom_tickers(cumulative_returns, n=3)

# Calculate rolling volatility
volatility_5day = rolling_volatility(portfolio, window=5)
```

### Running Tasks

**Task 3 - Portfolio Construction Methods**:

```bash
python task03.py
```

**Task 4 - Portfolio Analysis**:

```bash
python task04.py
```

**Run Tests**:

```bash
python -m pytest tests/test_portfolio_public.py -v
```

## 📈 Task Results

### Task 3: Portfolio Construction Methods

- **Symbols**: ['XOM', 'GOOG', 'AAPL', 'IBM', 'W']
- **Date Range**: August 1-14, 2020 (14 days)
- **Methods**: Join, Merge, and Concat
- **Output**: Three CSV files demonstrating equivalent results

### Task 4: Portfolio Analysis

- **Daily Returns**: Percentage changes between consecutive trading days
- **Cumulative Returns**: Total returns over the period
- **Performance Ranking**: Top and bottom performers identified
- **Volatility Analysis**: 5-day rolling standard deviation

## 🔧 API Reference

### Core Functions

#### Portfolio Construction

- `get_portfolio_join(symbols, dates, how='left')` - Build portfolio using join
- `get_portfolio_merge(symbols, dates, how='left')` - Build portfolio using merge
- `get_portfolio_concat(symbols, dates, axis=1, join='outer')` - Build portfolio using concat

#### Financial Analysis

- `compute_daily_returns(portfolio_df)` - Calculate daily percentage returns
- `compute_cumulative_returns(portfolio_df)` - Calculate cumulative returns
- `top_bottom_tickers(cum_returns, n=3)` - Find top/bottom performers
- `rolling_volatility(portfolio_df, window=5)` - Calculate rolling volatility

#### Utility Functions

- `read_stock_data(symbol)` - Read stock data from CSV
- `random_subset(symbols, k=5, seed=None)` - Generate random portfolio subset
- `random_end_date(start_date, min_days=3, max_days=14, seed=None)` - Generate random end date

## 📊 Sample Results

### Portfolio Performance (Aug 1-14, 2020)

- **Best Performer**: W (Wayfair) - 12.13%
- **Worst Performer**: IBM - 0.36%
- **Average Return**: 4.11%
- **Return Volatility**: 4.69%

### Available Stocks

- AAPL (Apple Inc.)
- AMZN (Amazon.com Inc.)
- CVNA (Carvana Co.)
- GLD (SPDR Gold Trust)
- GOOG (Alphabet Inc.)
- IBM (International Business Machines)
- SPY (SPDR S&P 500 ETF)
- W (Wayfair Inc.)
- XOM (Exxon Mobil Corp.)

## 🧪 Testing

The project includes comprehensive tests in the `tests/` directory:

```bash
# Run all tests
python -m pytest tests/test_portfolio_public.py -v

# Run specific test
python -m pytest tests/test_portfolio_public.py::test_portfolio_builders -v
```

## 📝 Requirements

- Python 3.7+
- pandas
- numpy

"""
Task 04 -- Portfolio Analysis: Daily Returns, Cumulative Returns, and Performance Analysis

This script performs comprehensive portfolio analysis including:
1. Daily returns calculation using pct_change()
2. Cumulative returns calculation 
3. Top and bottom performers identification
4. Rolling volatility analysis (optional)
5. Export results to CSV files

Uses the same portfolio from Task 03 for consistency.
"""

import pandas as pd
from get_portfolio import (
    get_portfolio_join,
    compute_daily_returns,
    compute_cumulative_returns,
    top_bottom_tickers,
    rolling_volatility,
    random_end_date
)

def main():
    """Perform comprehensive portfolio analysis and export results."""
    
    # Use the same portfolio from Task 03 for consistency
    symbols = ['XOM', 'GOOG', 'AAPL', 'IBM', 'W']
    start_date = "2020-08-01"
    
    # Compute end date using random_end_date (same as Task 03)
    end_date, delta_days = random_end_date(start_date, min_days=3, max_days=14, seed=42)
    
    # Create date range
    dates = pd.date_range(start_date, end_date, freq='D')
    
    print(f"Portfolio symbols: {symbols}")
    print(f"Date range: {start_date} to {end_date.strftime('%Y-%m-%d')} ({len(dates)} days)")
    print()
    
    # Build portfolio using join method
    portfolio = get_portfolio_join(symbols, dates, how='left')
    print(f"Portfolio shape: {portfolio.shape}")
    print(f"Portfolio columns: {list(portfolio.columns)}")
    print()
    
    # 1. Calculate daily returns
    print("1. Calculating daily returns...")
    daily_returns = compute_daily_returns(portfolio)
    print(f"Daily returns shape: {daily_returns.shape}")
    print("Sample daily returns:")
    print(daily_returns.head())
    print()
    
    # 2. Calculate cumulative returns
    print("2. Calculating cumulative returns...")
    cumulative_returns = compute_cumulative_returns(portfolio)
    print("Cumulative returns:")
    print(cumulative_returns)
    print()
    
    # 3. Identify top and bottom performers
    print("3. Identifying top and bottom performers...")
    top_performers, bottom_performers = top_bottom_tickers(cumulative_returns, n=3)
    print(f"Top 3 performers: {top_performers}")
    print(f"Bottom 3 performers: {bottom_performers}")
    print()
    
    # Display performance details
    print("Performance Details:")
    print("-" * 30)
    for ticker in top_performers:
        print(f"{ticker}: {cumulative_returns[ticker]:.4f} ({cumulative_returns[ticker]*100:.2f}%)")
    print()
    for ticker in bottom_performers:
        print(f"{ticker}: {cumulative_returns[ticker]:.4f} ({cumulative_returns[ticker]*100:.2f}%)")
    print()
    
    # 4. Optional: Rolling volatility analysis
    print("4. Rolling volatility analysis...")
    
    # 5-day rolling volatility
    rolling_vol_5 = rolling_volatility(portfolio, window=5)
    print("5-day rolling volatility (sample):")
    print(rolling_vol_5.head(10))
    print()
    
    # 50-day rolling volatility (if we have enough data)
    if len(daily_returns) >= 50:
        rolling_vol_50 = rolling_volatility(portfolio, window=50)
        print("50-day rolling volatility (sample):")
        print(rolling_vol_50.head(10))
    else:
        print(f"Not enough data for 50-day rolling volatility (need 50 days, have {len(daily_returns)})")
    print()
    
 
    # Export daily returns
    daily_returns.to_csv('task04_daily_returns.csv')
    print(f"✓ Daily returns saved to task04_daily_returns.csv")
    
    # Export cumulative returns (convert Series to DataFrame for CSV)
    cum_returns_df = cumulative_returns.to_frame('Cumulative_Return')
    cum_returns_df.to_csv('task04_cum_returns.csv')
    print(f"✓ Cumulative returns saved to task04_cum_returns.csv")
    
    # Optional: Export rolling volatility
    rolling_vol_5.to_csv('task04_rolling_volatility_5day.csv')
    print(f"✓ 5-day rolling volatility saved to task04_rolling_volatility_5day.csv")

    

if __name__ == "__main__":
    main()

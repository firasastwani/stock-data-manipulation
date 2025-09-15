"""
Task 03 -- Understanding join, merge & concat

Create portfolios using three different methods:
1. get_portfolio_join() using join()
2. get_portfolio_merge() using merge()  
3. get_portfolio_concat() using concat()

Symbols: ['XOM', 'GOOG', 'AAPL', 'IBM', 'W']
Dates: Start 08/01/2020, End computed using random_end_date from Task 2b
"""

import pandas as pd
from get_portfolio import (
    get_portfolio_join, 
    get_portfolio_merge, 
    get_portfolio_concat,
    random_end_date
)

def main():
    """Generate portfolios using all three methods and save as CSV files."""
    
    # Define symbols as specified
    symbols = ['XOM', 'GOOG', 'AAPL', 'IBM', 'W']
    print(f"Symbols: {symbols}")
    
    # Start date as specified
    start_date = "2020-08-01"
    print(f"Start date: {start_date}")
    
    # Compute end date using random_end_date (Task 2b)
    end_date, delta_days = random_end_date(start_date, min_days=3, max_days=14, seed=42)
    print(f"End date: {end_date} (delta: {delta_days} days)")
    
    # Create date range
    dates = pd.date_range(start_date, end_date, freq='D')
    print(f"Date range: {len(dates)} days")
    print()
    
    # Generate portfolios using all three methods
    print("Generating portfolios...")
    
    # 1. Using join method
    print("1. Generating portfolio using join method...")
    portfolio_join = get_portfolio_join(symbols, dates, how='left')
    portfolio_join.to_csv('task03a_join.csv')
    print(f"   Saved to task03a_join.csv")
    print(f"   Shape: {portfolio_join.shape}")
    print(f"   Columns: {list(portfolio_join.columns)}")
    print()
    
    # 2. Using merge method
    print("2. Generating portfolio using merge method...")
    portfolio_merge = get_portfolio_merge(symbols, dates, how='left')
    portfolio_merge.to_csv('task03b_merge.csv')
    print(f"   Saved to task03b_merge.csv")
    print(f"   Shape: {portfolio_merge.shape}")
    print(f"   Columns: {list(portfolio_merge.columns)}")
    print()
    
    # 3. Using concat method
    print("3. Generating portfolio using concat method...")
    portfolio_concat = get_portfolio_concat(symbols, dates, axis=1, join='outer')
    portfolio_concat.to_csv('task03c_concat.csv')
    print(f"   Saved to task03c_concat.csv")
    print(f"   Shape: {portfolio_concat.shape}")
    print(f"   Columns: {list(portfolio_concat.columns)}")
    print()
    
    # Display sample data from each method
    print("Sample data from each method:")
    print("=" * 50)
    
    print("\nJoin method (first 5 rows):")
    print(portfolio_join.head())
    
    print("\nMerge method (first 5 rows):")
    print(portfolio_merge.head())
    
    print("\nConcat method (first 5 rows):")
    print(portfolio_concat.head())
    
    # Check if all methods produce similar results
    print("\nComparison:")
    print("=" * 30)
    print(f"All methods have same shape: {portfolio_join.shape == portfolio_merge.shape == portfolio_concat.shape}")
    print(f"All methods have same columns: {list(portfolio_join.columns) == list(portfolio_merge.columns) == list(portfolio_concat.columns)}")
    
    # Check for differences in data
    join_merge_diff = (portfolio_join != portfolio_merge).sum().sum()
    join_concat_diff = (portfolio_join != portfolio_concat).sum().sum()
    merge_concat_diff = (portfolio_merge != portfolio_concat).sum().sum()
    
    print(f"Differences between join and merge: {join_merge_diff}")
    print(f"Differences between join and concat: {join_concat_diff}")
    print(f"Differences between merge and concat: {merge_concat_diff}")
    
    print("\nTask 03 completed successfully!")
    print("Generated files:")
    print("- task03a_join.csv")
    print("- task03b_merge.csv") 
    print("- task03c_concat.csv")

if __name__ == "__main__":
    main()

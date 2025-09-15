import pandas as pd
from get_portfolio import get_portfolio_join, random_subset

def test_simple_portfolio():
    """Simple test to print portfolio data for GOOG and AAPL"""
    

    # Create test dates
    dates = pd.date_range('2020-03-31', '2020-07-29', freq='D')
    
    # Test symbols
    symbols = ['GOOG', 'AAPL']
    print(f"Symbols: {symbols}")
    print()
    

    result = get_portfolio_join(symbols, dates, how='left')
    
 
    # Save the result DataFrame to 'task01a.csv'
    #result.to_csv('task01a.csv')
    print("Portfolio data saved to task01a.csv")
    print(result)

    symbols = ['SPY','CVNA','XOM','AMZN','GLD']

    result = get_portfolio_join(symbols, dates, how= 'left')
    #result.to_csv('task01b.csv')
    print(result)


def test_random_portfolio(): 
    """Test the random_subset function"""
    
    print("Testing random_subset function...")
    print("=" * 40)
    
    symbols = ['AAPL', 'AMZM', 'CVNA', 'GLD', 'GOOG', 'IBM', 'SPY', 'W', 'XOM']
    print(f"Available symbols: {symbols}")
    print()
    
    subset = random_subset(symbols, k=5)
    print(f"Random subset (k=5, seed=42): {subset}")
    print(f"Length: {len(subset)}")
    print()
    
    subset = random_subset(symbols, k=5)
    print(f"Random subset (k=5, seed=42): {subset}")
    print(f"Length: {len(subset)}")
    print()
     

    """
    # Test with different k value
    subset2 = random_subset(symbols, k=3)
    print(f"Random subset (k=3, seed=42): {subset2}")
    print(f"Length: {len(subset2)}")
    print()
    
    # Test without seed (should be different each time)
    subset3 = random_subset(symbols, k=4)
    print(f"Random subset (k=4, no seed): {subset3}")
    print(f"Length: {len(subset3)}")
    print()
    
    subset4 = random_subset(symbols, k=15)
    print(f"Random subset (k=15, seed=42): {subset4}")
    print(f"Length: {len(subset4)}")
    print()
    """
    
if __name__ == "__main__":

    #test_simple_portfolio()
    test_random_portfolio()

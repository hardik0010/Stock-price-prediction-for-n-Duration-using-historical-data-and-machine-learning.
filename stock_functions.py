from yahooquery import Ticker

def get_stock_symbol(filename="stocks_gen.txt"):
    """
    Searches for a stock symbol based on the company name.
    If multiple matches are found, it prompts the user to choose one.
    Returns the selected stock symbol with ".NS" suffix if it's an Indian stock.
    """
    company_name = input("Enter a Stock Name: ")
    stock_data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if ": " in line:
                    try:
                        name, symbol = line.split(": ", 1)  # Split at first ": " only
                        stock_data[name.lower()] = symbol
                    except ValueError:
                        pass  # Ignore malformed lines
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None

    company_name = company_name.strip().lower()
    matching_stocks = [name for name in stock_data if company_name in name]

    if len(matching_stocks) == 0:
        return None
    elif len(matching_stocks) == 1:
        return is_indian(stock_data[matching_stocks[0]])
    else:
        print("Multiple matches found. Please select:")
        for idx, stock in enumerate(matching_stocks, 1):
            print(f"{idx}. {stock}")
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(matching_stocks):
                return is_indian(stock_data[matching_stocks[choice - 1]])
        except ValueError:
            pass  # Invalid input, return None
    return None

def is_indian(stock_name):
    """
    Determines if the given stock is an Indian stock.
    If it's an Indian stock, returns the symbol with ".NS".
    Otherwise, returns the original symbol.
    """
    # First, try without ".NS" suffix
    ticker = Ticker(stock_name)
    if ticker.price and any("regularMarketPrice" in v for v in ticker.price.values()):
        return stock_name  # Valid non-Indian stock
    
    # Try with ".NS" suffix for Indian stocks
    indian_symbol = stock_name + ".NS"
    ticker = Ticker(indian_symbol)
    if ticker.price and any("regularMarketPrice" in v for v in ticker.price.values()):
        return indian_symbol  # Valid Indian stock with ".NS" suffix
    
    return None  # Invalid stock symbol


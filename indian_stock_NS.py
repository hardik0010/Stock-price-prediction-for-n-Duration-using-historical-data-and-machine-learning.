from yahooquery import Ticker

while True:
    stock_symbol = input("Enter stock symbol (e.g. AAPL for Apple, or the stock name for Indian stocks): ").strip()

    try:
        # First, try without ".NS" suffix
        ticker = Ticker(stock_symbol)
        if ticker.price and stock_symbol in ticker.price:
            print(f"Stock symbol {stock_symbol} is valid.")
            break  # Exit the loop if the symbol is valid
        else:
            # If no valid symbol, check by adding ".NS" for Indian stocks
            stock_symbol = stock_symbol + ".NS"
            ticker = Ticker(stock_symbol)
            if ticker.price and stock_symbol in ticker.price:
                print(f"Stock symbol {stock_symbol} is valid.")
                break  # Exit the loop if the symbol with ".NS" is valid
            else:
                print(f"Invalid stock symbol {stock_symbol}. Please enter a valid symbol.")
    except Exception as e:
        print(f"An error occurred while validating the stock symbol. Please try again. Error: {e}")

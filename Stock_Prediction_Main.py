from yahooquery import Ticker
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplcursors
from matplotlib.ticker import MaxNLocator
import stock_functions

stock_symbol = stock_functions.get_stock_symbol()
try:
    ticker = Ticker(stock_symbol)
    if ticker.price:
        pass
    else:
        stock_symbol = input("No stock found, try entering stock symbol: ")
except:
    stock_symbol = input("No stock found, try entering stock symbol: ")

while True:
    target_date = input("Enter the target date (YYYY-MM-DD): ")
    try:
        target_date_obj = datetime.strptime(target_date, '%Y-%m-%d')
        if target_date_obj >= datetime.today():
            break
        else:
            print("Please enter a future date.")
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")

start_date = "2022-01-01"
end_date = target_date

try:
    data = ticker.history(start=start_date, end=end_date)

    if data.empty:
        print("No price data found for the entered stock symbol.")
    else:
        data = data.reset_index()
        data['Date'] = data['date'].apply(lambda x: datetime.combine(x, datetime.min.time()).timestamp()).astype(int)
        X = np.array(data['Date']).reshape(-1, 1)
        y = np.array(data['close'])

        model = LinearRegression()
        model.fit(X, y)

        target_date_timestamp = datetime.strptime(target_date, '%Y-%m-%d').timestamp()
        predicted_price = model.predict(np.array([[target_date_timestamp]]))[0]
        y_pred = model.predict(X)

        r2 = r2_score(y, y_pred)
        current_price = ticker.history(period="1d")["close"].iloc[0]

        target_date_num = mdates.date2num(datetime.strptime(target_date, '%Y-%m-%d'))

        plt.figure(figsize=(10, 6))
        plt.plot(data['date'], data['close'], color='blue', label='Historical Prices')
        plt.scatter(target_date_num, predicted_price, color='green', marker='o', s=100, label='Predicted Price')
        plt.scatter(data['date'].iloc[-1], current_price, color='red', marker='o', s=100, label='Current Price')

        plt.title(f'{stock_symbol} Stock Price')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=12))  # Ensure only 10 x-axis values
        plt.gcf().autofmt_xdate()

        is_indian_stock = stock_symbol.endswith('.NS')
        currency_symbol = '₹' if is_indian_stock else '$'

        cursor = mplcursors.cursor(hover=True)
        cursor.connect("add", lambda sel: sel.annotation.set_text(f"Value: {currency_symbol}{sel.target[1]:.2f}"))

        plt.show()

        print(f"Predicted {stock_symbol} price on {target_date}: {currency_symbol}{predicted_price:.2f}")
        print(f"Current {stock_symbol} price: {currency_symbol}{current_price:.2f}")
        print(f"Accuracy: {r2:.4f}")
except Exception as e:
    print(f"An error occurred: {e}")
# Stock-price-prediction-for-n-Duration-using-historical-data-and-machine-learning.
A machine learning project that predicts stock prices for a given future date using historical data.   Uses Linear Regression with `yahooquery` for fetching stock data and `matplotlib` for visualization.  

# 📈 Stock Price Prediction Using Linear Regression

This Python project predicts future stock prices using **Linear Regression** based on historical stock data.  
It fetches **real-time stock data** using `yahooquery` and visualizes trends using `matplotlib`.  

## 🚀 Features
- Fetches **real-time** stock prices using `yahooquery`
- Predicts future prices using **Linear Regression (scikit-learn)**
- Supports both **Indian (NSE) & Global (NYSE, NASDAQ) stocks**
- **Plots historical stock prices** with prediction markers
- Displays **prediction accuracy (R² score)**  

---

## 📦 Dependencies
Make sure you have Python installed. Then install the required libraries:  
```sh
pip install yahooquery numpy scikit-learn matplotlib

🔧 How to Run
Run the script in a terminal or command prompt:
python stock_price_prediction.py

Then enter:
Stock Symbol (e.g., AAPL for Apple, RELIANCE.NS for Indian stocks)
Target Date (YYYY-MM-DD format for prediction)


📊 Example Output
Enter stock symbol: AAPL
Enter target date (YYYY-MM-DD): 2025-03-01
Predicted AAPL price on 2025-03-01: $192.43
Current AAPL price: $186.50
Accuracy: 0.8795

A graph will also appear, showing:
✅ Historical Prices (Blue Line)
✅ Current Price (Red Marker)
✅ Predicted Price (Green Marker)

📌 How It Works
Fetches historical stock data from yahooquery
Converts dates into numerical timestamps
Trains a Linear Regression model using past data
Predicts stock price for the user-entered future date
Plots results using matplotlib

🔮 Future Enhancements
🔹 Use Deep Learning Models (LSTMs, RNNs) for better predictions
🔹 Analyze financial news & social media for sentiment-based forecasting
🔹 Deploy as a Web App (Flask, Streamlit)
🔹 Allow multi-stock comparison for investment insights

👨‍💻 Author
Gajjar Hardik
📧 Contact: 9687219575
🔗 GitHub: https://github.com/hardik0010

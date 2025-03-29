# AI Trading Bot using LumiBot, Alpaca & FinBERT   

## 📌 Overview  
This AI-powered **algorithmic trading bot** utilizes **sentiment analysis** and **machine learning** to execute trades automatically based on real-time market news. It integrates **LumiBot** for strategy execution, **Alpaca API** for order placement, and **FinBERT** for financial sentiment analysis.

## 🚀 Features  
✅ **Sentiment-Based Trading**: Uses FinBERT to analyze financial news and determine market sentiment.  
✅ **Automated Trading**: Places buy/sell orders based on sentiment probability and trading strategy.  
✅ **Backtesting Support**: Simulates past trades using historical market data via **Yahoo Finance**.  
✅ **Risk Management**: Implements bracket orders with **stop-loss and take-profit** levels.  
✅ **Logging & Data Storage**:  
   - Saves **trade logs** in the `/logs` folder.  
   - Exports data in **JSON, HTML, and Excel formats** for later analysis.  

---

## 🔧 Installation  
Ensure you have **Python 3.8+** installed, then run:  
```sh
pip install -r requirements.txt
```

---

## 📜 Usage  

### 1️⃣ **Run Backtesting (Simulated Trading)**  
```sh
python trading_bot.py
```
This will backtest the strategy using historical data and log the results.  

### 2️⃣ **Run Live Trading (Real Market Execution)**  
Modify the script to **disable backtesting** and enable live trading, then execute:  
```sh
python trading_bot.py
```
This will execute trades in **real-time** based on financial news sentiment.  

---

## ⚙️ How It Works  
1. **Fetches financial news** related to a selected stock from the Alpaca API.  
2. **Uses FinBERT** to estimate sentiment (positive/negative/neutral) from the news.  
3. If **sentiment is highly positive**, it places a **BUY** order with a **take-profit and stop-loss** strategy.  
4. If **sentiment is highly negative**, it places a **SELL** order following a similar risk-managed approach.  
5. **Updates logs and saves trade history** after every trade execution.  

---

## 📂 File Structure  
```
├── trading_bot.py          # Main Trading Bot Script
├── sentiment.py       # FinBERT Sentiment Analysis
├── logs/              # Stores trade logs in JSON, HTML, Excel
├── requirements.txt   # Dependencies List
├── README.md          # Project Documentation
```

---

## 📦 Dependencies  
All required dependencies are listed in `requirements.txt`. Install them using:  
```sh
pip install -r requirements.txt
```

### 📜 `requirements.txt` (Dependencies List)  
```sh
numpy
pandas
torch
transformers
timedelta
alpaca-trade-api
lumibot
pygame
openpyxl
```

---

## 📊 Logging & Data Storage  
The bot **automatically saves analysis and trading logs** in the `/logs/` folder in the following formats:  
📌 **JSON** – Stores structured trade execution data.  
📌 **HTML** – Generates an easy-to-read trading report.  
📌 **Excel** – Saves trade performance analysis for further evaluation.  

---

## ⚠️ Disclaimer  
This bot is for **educational purposes only**. Trading involves risk, and past performance is not indicative of future results. Use at your own discretion.

---

Developed with ❤️ by Harikrishna Rao

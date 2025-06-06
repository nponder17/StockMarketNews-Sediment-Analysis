import requests
import pandas as pd
from datetime import datetime

def get_stocktwits_messages(ticker, limit=30):
    url = f"https://api.stocktwits.com/api/2/streams/symbol/{ticker}.json"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return []

    messages = response.json().get('messages', [])
    results = []

    for msg in messages[:limit]:
        results.append({
            "Username": msg["user"]["username"],
            "Date": msg["created_at"],
            "Message": msg["body"],
            "Source": "StockTwits",
            "Symbol": ticker
        })

    return results

tickers = ['AAPL', 'TSLA', 'NVDA', 'GOOGL', 'AMZN', 'MSFT', 'META', 'CRWD', 'NFLX', 'AMD']
allMessages = []

for ticker in tickers:
    print(f"Searching messages for {ticker}")
    messages = get_stocktwits_messages(ticker)
    allMessages.extend(messages)

df = pd.DataFrame(allMessages)

print(df)
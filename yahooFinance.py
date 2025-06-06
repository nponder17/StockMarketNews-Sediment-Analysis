import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

def get_yahoo_news(ticker, limit=10):
    url = f'https://finance.yahoo.com/quote/{ticker}/news?p={ticker}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch news for {ticker}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.select('li.js-stream-content')[:limit]

    results = []
    for article in articles:
        headline = article.select_one('h3').text if article.select_one('h3') else "No title"
        link = 'https://finance.yahoo.com' + article.select_one('a')['href']
        date_span = article.select_one('span[class*="C(#959595)"]')
        date_text = date_span.text if date_span else "Unknown"

        results.append({
            "Ticker": ticker,
            "Headline": headline,
            "URL": link,
            "Date": date_text,
            "Source": "Yahoo Finance"
        })

    return results

tickers = ['AAPL', 'TSLA', 'NVDA', 'GOOGL', 'AMZN', 'MSFT', 'META', 'CRWD', 'NFLX', 'AMD']
allNews = []

for ticker in tickers:
    print(f"Fetching news for {ticker}")
    news = get_yahoo_news(ticker)
    allNews.extend(news)
    time.sleep(1)  

df = pd.DataFrame(allNews)

print(df)
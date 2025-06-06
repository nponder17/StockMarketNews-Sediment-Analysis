# StockMarketNews-Sediment-Analysis

This project aims to gather stock-related news from multiple sources, including Reddit, Yahoo Finance, Twitter, and StockTwits. The collected data is analyzed using sentiment analysis tools like VADER and FinBERT to classify the sentiment of the posts (positive, negative, neutral).

Overview
Initially, the project only focused on pulling Reddit posts related to stocks and running sentiment analysis using VADER and FinBERT. However, it has since expanded to include additional sources like Yahoo Finance, Twitter, and StockTwits to provide a broader perspective on market sentiment.

File Descriptions
pullPosts.py: This script collects stock-related posts from Reddit using the Reddit API.

yahooFinance.py: Collects stock-related news from Yahoo Finance using web scraping or the Yahoo Finance API.

sentimentAnalysis.py: Analyzes the sentiment of the collected text data using VADER sentiment analysis.

finbertAnalysis.py: Performs sentiment analysis using the FinBERT model, specifically fine-tuned for financial news.

pullStockTwits.py: Collects posts from StockTwits related to stocks using their API.

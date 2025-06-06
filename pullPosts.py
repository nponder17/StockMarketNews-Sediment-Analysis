import praw
import pandas as pd
from datetime import datetime
from sentimentAnalysis import analyze_sentiment
from finbertAnalysis import analyze_finbert_sentiment


reddit = praw.Reddit(
    client_id='0YlSqHy13CXlficefjfmTQ',
    client_secret='N0Sexny9hzcPPWuA5TgXAwDCcBHBwA',
    user_agent='SentimentScraper by u/Brief_Leg_150'
)

subreddits = ['stocks', 'investing', 'wallstreetbets']

#queries = ['AAPL', 'Apple', 'TSLA',  'Tesla', 'NVDA', 'Nvidia']
queryMap = {
    'AAPL': ['AAPL', 'Apple'],
    'TSLA': ['TSLA', 'Tesla'],
    'NVDA': ['NVDA', 'Nvidia'],
    'GOOGL': ['GOOGL', 'GOOG', 'Google', 'Alphabet'],
    'AMZN': ['AMZN', 'Amazon'],
    'MSFT': ['MSFT', 'Microsoft'],
    'META': ['META', 'Facebook', 'Meta'],
    'CRWD': ['CRWD', 'CrowdStrike'],
    'NFLX': ['NFLX', 'Netflix'],
    'AMD': ['AMD', 'Advanced Micro Devices'],
    '^GSPC': ['S&P 500', 'S&P', 'SP500', 'SPX'] 
}

sentimentKeywords = ['buy', 'sell', 'forecast', 'prediction']

seenPosts = []

#check each subreddit we want
for sub in subreddits:
    subreddit = reddit.subreddit(sub)

    #loop through each query for stocks you desire
    
    for ticker, searchWords in queryMap.items():
        print(f"Searching r/{sub} for: {ticker}")

        for word in searchWords:

            # Perform the search and retrieve posts


            for post in subreddit.search(word, sort='new', time_filter='day', limit=20):
                combinedText = post.title + post.selftext
                #avoid duplicate posts
                if post.title in (seenPost['Title'] for seenPost in seenPosts):
                    continue
                if any(searchWord.lower() in post.title.lower() for searchWord in searchWords):
                    if any(keyword.lower() in combinedText.lower() for keyword in sentimentKeywords):
                        sentiment_label, sentiment_score = analyze_sentiment(post.title + " " + post.selftext)
                        finbertAnalysisLabel, finbertAnalysisScore = analyze_finbert_sentiment(post.title + " " + post.selftext)
                        seenPosts.append({
                            "Subreddit": sub,
                            "Ticker": ticker,
                            "Title": post.title,
                            "Score": post.score,
                            "Date Posted": datetime.utcfromtimestamp(post.created_utc),
                            "URL": post.url,
                            "Text": post.selftext,
                            "Vader Sentiment Label": sentiment_label,
                            "Vader Sentiment Score": sentiment_score,
                            "Finbert Analysis Label" : finbertAnalysisLabel,
                            "Finbert Analysis Score" : finbertAnalysisScore
                        })


df = pd.DataFrame(seenPosts)
print(df)

#uncomment to produce csv file
#today = datetime.today().strftime('%Y-%m-%d')
#df.to_csv(f'reddit_sentiment_{today}.csv', index=False)





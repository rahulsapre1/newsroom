from datetime import datetime, timedelta
from serpapi import GoogleSearch
import os

def search_news(topic, api_key):
    """Search for news articles on the given topic using SerpAPI"""
    print(f"Searching for news about '{topic}'...")
    
    # Calculate date for last 24 hours
    yesterday = datetime.now() - timedelta(days=1)
    date_str = yesterday.strftime("%Y-%m-%d")
    
    # Set up the search parameters
    params = {
        "engine": "google_news",
        "q": topic,
        "tbm": "nws",
        "tbs": f"cdr:1,cd_min:{date_str},cd_max:today",  # Last 24 hours
        "num": 10,  # Strictly limit to 10 results
        "api_key": api_key,
        "hl": "en",  # English language
        "gl": "in"   # US region for better news coverage
    }
    
    # Execute the search
    search = GoogleSearch(params)
    results = search.get_dict()
    
    # Check if we have news results
    if "news_results" not in results:
        print("No news found for this topic in the last 24 hours.")
        return []
    
    # Ensure we only return up to 10 results
    news_results = results["news_results"][:10]
    
    # Print the number of articles found
    print(f"Found {len(news_results)} articles from the last 24 hours.")
    
    return news_results 
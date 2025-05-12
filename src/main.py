import os
from dotenv import load_dotenv
from newsroom import search_news, summarize_news

def get_topic():
    """Ask the user for a news topic to search for"""
    topic = input("Enter a topic to get news about: ")
    return topic

def get_daily_news():
    """Main function to run the news summarizer"""
    # Load environment variables
    load_dotenv()
    
    # Get API keys
    SERPAPI_KEY = os.getenv('SERP_AI_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    if not SERPAPI_KEY or not OPENAI_API_KEY:
        raise ValueError("API keys not found in .env file. Please check your .env file configuration.")
    
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    
    # Get topic from user
    topic = get_topic()
    
    # Search for news
    articles = search_news(topic, SERPAPI_KEY)
    
    if not articles:
        return "No news found for this topic in the last 24 hours."
    
    # Summarize the news
    summary = summarize_news(articles)
    
    print("\n" + "="*50)
    print(f"TOP NEWS SUMMARY FOR: {topic.upper()}")
    print("="*50)
    print(summary)
    print("="*50)
    
    return summary

if __name__ == "__main__":
    get_daily_news() 
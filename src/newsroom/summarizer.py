import litellm
from .content_extractor import extract_article_content

def summarize_news(articles):
    """Summarize the news articles using LiteLLM"""
    if not articles:
        return "No news articles found to summarize."
    
    print("Collecting and summarizing news articles...")
    
    # Prepare context for the LLM
    article_texts = []
    # Process only top 5 articles for better quality summary
    for i, article in enumerate(articles[:5]):
        title = article.get("title", "No title")
        source = article.get("source", "Unknown source")
        link = article.get("link", "")
        snippet = article.get("snippet", "")
        
        print(f"Processing article {i+1}: {title}")
        
        # Get full content if possible
        content = extract_article_content(link)
        if not content:
            content = snippet  # Fall back to snippet if extraction fails
            
        article_texts.append(f"ARTICLE {i+1}:\nTitle: {title}\nSource: {source}\nContent: {content}\n")
    
    # Combine all articles
    all_articles = "\n\n".join(article_texts)
    
    # Create prompt for the LLM
    prompt = f"""Based on the following news articles from the last 24 hours, provide a concise summary highlighting the 3 most important things someone should know about this topic and why they matter. Format your response as a numbered list (1, 2, 3) with a brief explanation for each point.\n\n{all_articles}"""
    
    # Call LiteLLM to summarize
    try:
        response = litellm.completion(
            model="gpt-4",  # Fixed model name
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in LLM summarization: {e}")
        return "Error generating summary. Please check your API keys and try again." 
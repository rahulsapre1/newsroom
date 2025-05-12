import streamlit as st
import os
from dotenv import load_dotenv
from newsroom import search_news, summarize_news

# Page config
st.set_page_config(
    page_title="Newsroom - Daily News Summarizer",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Improved CSS for cards and summary
st.markdown("""
    <style>
    /* Main container */
    .main {
        padding: 2rem;
        background-color: #f8f9fa;
    }
    
    /* Title styling */
    h1 {
        color: #1f1f1f;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }
    
    /* Input styling */
    .stTextInput>div>div>input {
        font-size: 1.2rem;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 0.5rem 1rem;
    }
    
    /* Article cards */
    .article-card {
        background: #fff;
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        margin-bottom: 1.5rem;
        min-height: 220px;
        max-height: 220px;
        height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: 1px solid #ececec;
        transition: box-shadow 0.2s;
        overflow: hidden;
    }
    
    .article-card:hover {
        box-shadow: 0 6px 18px rgba(0,0,0,0.13);
    }
    
    .article-title {
        color: #1a1a1a;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 5;
        -webkit-box-orient: vertical;
    }
    
    .article-source {
        color: #666;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    
    .article-description {
        color: #444;
        font-size: 0.98rem;
        margin-bottom: 0.5rem;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
    
    .article-link {
        color: #0066cc;
        text-decoration: none;
        font-weight: 500;
        margin-top: auto;
    }
    
    /* Summary box */
    .summary-box {
        background: #f8f9fa;
        color: #222;
        padding: 2rem;
        border-radius: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        margin: 1.5rem 0;
        font-size: 1.15rem;
        line-height: 1.7;
    }
    .summary-box ol {
        padding-left: 1.5rem;
        margin-left: 0;
    }
    .summary-box ol li {
        text-indent: 0;
        padding-left: 0;
        margin-bottom: 1rem;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        white-space: normal;
    }
    
    /* Loading spinner */
    .stSpinner {
        margin: 2rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #666;
        margin-top: 3rem;
        padding: 1rem;
        border-top: 1px solid #e0e0e0;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    .stColumns {
        gap: 1.5rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    st.markdown("---")
    
    # Date range selector
    st.subheader("📅 Time Range")
    time_range = st.selectbox(
        "Select time range",
        ["Last 24 hours", "Last 48 hours", "Last week"],
        index=0
    )
    
    # Number of articles
    st.subheader("📊 Display Options")
    num_articles = st.slider(
        "Number of articles to display",
        min_value=3,
        max_value=10,
        value=5
    )
    
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center'>
            <p>Made with ❤️ by Newsroom</p>
        </div>
    """, unsafe_allow_html=True)

# Main content
st.title("📰 Newsroom")
st.markdown("""
    <div style='font-size: 1.2rem; color: #666; margin-bottom: 2rem;'>
        Get instant summaries of the most important news from the last 24 hours.
        Enter a topic below to get started.
    </div>
""", unsafe_allow_html=True)

# Load environment variables
load_dotenv()

# Get API keys
SERPAPI_KEY = os.getenv('SERP_AI_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not SERPAPI_KEY or not OPENAI_API_KEY:
    st.error("API keys not found in .env file. Please check your configuration.")
    st.stop()

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Search input with a nice container
with st.container():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        topic = st.text_input(
            "🔍 Search for news about:",
            placeholder="e.g., Artificial Intelligence, Climate Change, etc.",
            key="search_input"
        )

if topic:
    with st.spinner("🔍 Searching for the latest news articles..."):
        articles = search_news(topic, SERPAPI_KEY)
        # Filter out articles with 'Unknown source'
        filtered_articles = [a for a in articles[:num_articles] if a.get('source', 'Unknown source') != 'Unknown source']
        if not filtered_articles:
            st.warning("⚠️ No news found for this topic in the last 24 hours.")
        else:
            st.subheader("📑 Latest Articles")
            cols = st.columns(3)
            for i, article in enumerate(filtered_articles):
                with cols[i % 3]:
                    st.markdown(f"""
                        <div class='article-card'>
                            <div class='article-title'>{article.get('title', 'No title')}</div>
                            <a href='{article.get('link', '#')}' target='_blank' class='article-link'>Read full article →</a>
                        </div>
                    """, unsafe_allow_html=True)
            with st.spinner("🤖 Generating AI-powered summary..."):
                summary = summarize_news(articles)
                st.subheader("📝 AI Summary")
                st.markdown(
                    f"<div class='summary-box'>{summary}</div>",
                    unsafe_allow_html=True
                )

# Footer
st.markdown("""
    <div class='footer'>
        <p>Powered by SerpAPI and OpenAI GPT-4 | Made with Streamlit</p>
    </div>
""", unsafe_allow_html=True) 
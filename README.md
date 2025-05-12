# Newsroom - Daily News Summarizer

A Python application that searches for recent news articles on a given topic and provides a concise summary using AI. Available as both a CLI tool and a web interface.

## Features

- Search for recent news articles (last 24 hours)
- Extract and clean article content
- Generate AI-powered summaries
- Beautiful web interface using Streamlit
- Modular and extensible design

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv .news_env
source .news_env/bin/activate  # On Windows: .news_env\Scripts\activate
```

2. Install the package:
```bash
pip install -e .
```

3. Create a `.env` file in the project root with your API keys:
```
SERP_AI_API_KEY=your_serpapi_key
OPENAI_API_KEY=your_openai_key
```

## Usage

### Web Interface (Recommended)
Run the Streamlit app:
```bash
streamlit run src/app.py
```

### Command Line Interface
Run the CLI version:
```bash
python src/main.py
```

When prompted, enter a topic you want to get news about. The application will:
1. Search for recent news articles
2. Extract and process the content
3. Generate a summary of the 3 most important points

## Project Structure

```
newsroom/
├── .env                    # API keys
├── requirements.txt        # Dependencies
├── setup.py               # Package configuration
└── src/
    ├── app.py             # Streamlit web interface
    ├── main.py            # CLI script
    └── newsroom/          # Package
        ├── __init__.py
        ├── news_search.py
        ├── content_extractor.py
        └── summarizer.py
```

## Requirements

- Python 3.8 or higher
- SerpAPI key for news search
- OpenAI API key for summarization

## Improvements Made

1. Added Streamlit web interface with:
   - Clean, modern UI
   - Article cards with links
   - Loading spinners
   - Responsive layout
   - Custom styling

2. Enhanced news search:
   - Strict 24-hour time limit
   - Better article filtering
   - Region-specific news (India)
   - Improved error handling

3. Better summarization:
   - Focus on top 5 most relevant articles
   - Clearer formatting
   - More context in prompts 
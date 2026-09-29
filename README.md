# DataLens

DataLens is an AI-powered data analysis app that lets users upload CSV files and ask questions about their data using natural language.

Instead of manually writing Python or Pandas code, users can ask questions like:

* What is the average sales?
* Which category has the highest revenue?
* What are the top 5 products?
* Show the trend over time.

## How It Works

CSV → Streamlit → LangChain CSV Agent → Google Gemini → Python/Pandas → Insights

## Tech Stack

Python, Streamlit, Pandas, LangChain, Google Gemini, Matplotlib

## Setup

```bash
pip install -r requirements.txt
python3 -m streamlit run app.py
```

Create a `.env` file:

```text
GOOGLE_API_KEY=your_api_key_here
```

Keep your API key private and never commit `.env` to GitHub.

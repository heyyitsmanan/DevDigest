# DevDigest

DevDigest is a small Streamlit app that turns a webpage or article URL into a brief AI-generated summary. It fetches the page text with `requests` and Beautiful Soup, then sends that text to Groq using its OpenAI-compatible API.

## What it does

1. Paste an article URL into the app.
2. Click **Summarize** to fetch the page and generate a summary.
3. Read the result in the browser.

The API is called only after you click the button. Some sites may block automated requests, and pages whose main content is loaded by JavaScript may not extract well.

## Run locally

Use Python 3.10 or newer. From this project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install beautifulsoup4
```

Create a `.env` file in this directory with your Groq API key:

```dotenv
GROQ_API_KEY=your_key_here
```

Start the app:

```bash
python -m streamlit run summariser.py
```

Streamlit will show a local URL in the terminal. Open it in your browser, paste an article link, and click **Summarize**. When you are finished, stop the server with `Ctrl+C` and leave the virtual environment with `deactivate`.

## Project files

- `summariser.py`: Streamlit interface and Groq API request.
- `scraper.py`: Downloads a page and extracts readable text.
- `requirements.txt`: Pinned Python packages. `beautifulsoup4` is also needed by `scraper.py` but is not listed yet.
- `.env`: Your local API key. This file is ignored by Git; do not commit it.

AI-generated summaries can be inaccurate. Check the original article before relying on a summary.

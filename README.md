# NLP Sentiment Analysis Project

End-to-end sentiment analysis project using Groq API with Llama3 model and Streamlit deployment.

## Features

- **Modular Architecture**: Clean separation of concerns with dedicated modules
- **Multiple Input Methods**: Single text, multiple texts, or CSV upload
- **Real-time Analysis**: Powered by Groq API with Llama3/DeepSeek models
- **Interactive Dashboard**: Streamlit-based web interface
- **Visualization**: Sentiment distribution charts and summary statistics
- **Export Results**: Download analysis results as CSV

## Project Structure

```
├── app.py                 # Streamlit web application
├── pipeline.py            # Main orchestration pipeline
├── sentiment_analyzer.py  # Groq API integration for sentiment analysis
├── data_processor.py      # Text preprocessing and cleaning
├── config.py             # Configuration and settings
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (API keys)
└── README.md            # Project documentation
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

## Usage

1. **Single Text**: Enter one text for sentiment analysis
2. **Multiple Texts**: Enter multiple texts (one per line)
3. **CSV Upload**: Upload CSV file with 'text' column

## Models Available

- `llama-3.1-8b-instant` (default)
- `llama-3.1-70b-versatile`
- `mixtral-8x7b-32768`

Change model in `config.py` by updating `MODEL_NAME`.
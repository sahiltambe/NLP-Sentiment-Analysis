# https://github.com/sahiltambe/NLP-Sentiment-Analysis

import streamlit as st
import pandas as pd
import plotly.express as px
from pipeline import SentimentPipeline

st.set_page_config(page_title="NLP Sentiment Analysis", page_icon="🎭", layout="wide")

def main():
    st.title("🎭 NLP Sentiment Analysis")
    st.markdown("Analyze sentiment using Groq API with Llama3 model")
    
    # Initialize pipeline
    if 'pipeline' not in st.session_state:
        st.session_state.pipeline = SentimentPipeline()
    
    # Sidebar for input method selection
    st.sidebar.header("Input Method")
    input_method = st.sidebar.selectbox("Choose input method:", ["Single Text", "Multiple Texts", "Upload CSV"])
    
    results = []
    
    if input_method == "Single Text":
        text_input = st.text_area("Enter text to analyze:", height=100)
        if st.button("Analyze Sentiment") and text_input:
            with st.spinner("Analyzing sentiment..."):
                results = st.session_state.pipeline.run(text_input)
    
    elif input_method == "Multiple Texts":
        texts_input = st.text_area("Enter multiple texts (one per line):", height=200)
        if st.button("Analyze Sentiments") and texts_input:
            texts = [line.strip() for line in texts_input.split('\n') if line.strip()]
            with st.spinner("Analyzing sentiments..."):
                results = st.session_state.pipeline.run(texts)
    
    elif input_method == "Upload CSV":
        uploaded_file = st.file_uploader("Upload CSV file with 'text' column:", type=['csv'])
        if uploaded_file and st.button("Analyze CSV"):
            df = pd.read_csv(uploaded_file)
            with st.spinner("Analyzing sentiments..."):
                results = st.session_state.pipeline.run(df)
    
    # Display results
    if results:
        st.header("📊 Results")
        
        # Create DataFrame for display
        df_results = pd.DataFrame(results)
        
        # Summary statistics
        summary = st.session_state.pipeline.get_summary(results)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Summary")
            st.metric("Total Texts", len(results))
            st.metric("Positive", summary['positive'])
            st.metric("Negative", summary['negative'])
            st.metric("Neutral", summary['neutral'])
        
        with col2:
            st.subheader("Sentiment Distribution")
            fig = px.pie(values=list(summary.values()), names=list(summary.keys()),
                        color_discrete_map={'positive': 'green', 'negative': 'red', 'neutral': 'gray'})
            st.plotly_chart(fig, use_container_width=True)
        
        # Detailed results
        st.subheader("Detailed Results")
        st.dataframe(df_results, use_container_width=True)
        
        # Download results
        csv = df_results.to_csv(index=False)
        st.download_button("Download Results as CSV", csv, "sentiment_results.csv", "text/csv")

if __name__ == "__main__":
    main()
from data_processor import TextPreprocessor
from sentiment_analyzer import SentimentAnalyzer
from typing import List, Dict, Union
import pandas as pd

class SentimentPipeline:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.analyzer = SentimentAnalyzer()
    
    def run(self, data: Union[str, List[str], pd.DataFrame]) -> List[Dict[str, str]]:
        """Run the complete sentiment analysis pipeline"""
        # Step 1: Load and preprocess data
        processed_texts = self.preprocessor.load_data(data)
        
        # Step 2: Analyze sentiment
        results = self.analyzer.analyze_batch(processed_texts)
        
        return results
    
    def get_summary(self, results: List[Dict[str, str]]) -> Dict[str, int]:
        """Get summary statistics of sentiment analysis"""
        summary = {"positive": 0, "negative": 0, "neutral": 0}
        
        for result in results:
            sentiment = result.get("sentiment", "neutral")
            if sentiment in summary:
                summary[sentiment] += 1
        
        return summary
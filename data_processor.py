import re
import pandas as pd
from typing import List, Union

class TextPreprocessor:
    def __init__(self):
        self.url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        self.mention_pattern = re.compile(r'@\w+')
        self.hashtag_pattern = re.compile(r'#\w+')
    
    def clean_text(self, text: str) -> str:
        """Clean and preprocess text data"""
        if not isinstance(text, str):
            return ""
        
        # Remove URLs
        text = self.url_pattern.sub('', text)
        # Remove mentions
        text = self.mention_pattern.sub('', text)
        # Remove hashtags
        text = self.hashtag_pattern.sub('', text)
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text.strip()
    
    def process_batch(self, texts: List[str]) -> List[str]:
        """Process a batch of texts"""
        return [self.clean_text(text) for text in texts]
    
    def load_data(self, data: Union[str, List[str], pd.DataFrame]) -> List[str]:
        """Load and prepare data for processing"""
        if isinstance(data, str):
            return [self.clean_text(data)]
        elif isinstance(data, list):
            return self.process_batch(data)
        elif isinstance(data, pd.DataFrame):
            if 'text' in data.columns:
                return self.process_batch(data['text'].tolist())
            else:
                raise ValueError("DataFrame must have 'text' column")
        else:
            raise ValueError("Unsupported data type")
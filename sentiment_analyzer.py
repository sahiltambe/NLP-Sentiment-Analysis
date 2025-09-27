import requests
from typing import List, Dict
import json
from config import Config

class SentimentAnalyzer:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.model = Config.MODEL_NAME
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
    
    def analyze_single(self, text: str) -> Dict[str, str]:
        """Analyze sentiment of a single text"""
        prompt = f"""
Analyze the sentiment of the following text and return only a JSON response with 'sentiment' (positive/negative/neutral) and 'confidence' (high/medium/low):

Text: "{text}"

Response format: {{"sentiment": "positive/negative/neutral", "confidence": "high/medium/low"}}
"""
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": Config.MAX_TOKENS,
            "temperature": Config.TEMPERATURE
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()
            
            result = response.json()["choices"][0]["message"]["content"].strip()
            
            # Extract JSON from response
            if '{' in result and '}' in result:
                json_start = result.find('{')
                json_end = result.rfind('}') + 1
                json_str = result[json_start:json_end]
                return json.loads(json_str)
            else:
                return {"sentiment": "neutral", "confidence": "low"}
                
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return {"sentiment": "neutral", "confidence": "low"}
    
    def analyze_batch(self, texts: List[str]) -> List[Dict[str, str]]:
        """Analyze sentiment of multiple texts"""
        results = []
        for text in texts:
            if text.strip():
                result = self.analyze_single(text)
                result['text'] = text
                results.append(result)
            else:
                results.append({"text": text, "sentiment": "neutral", "confidence": "low"})
        return results
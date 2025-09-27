from pipeline import SentimentPipeline

def main():
    # Initialize pipeline
    pipeline = SentimentPipeline()
    
    # Example 1: Single text
    single_text = "I love this product! It's amazing and works perfectly."
    result = pipeline.run(single_text)
    print("Single text result:", result)
    
    # Example 2: Multiple texts
    texts = [
        "This is the worst service ever!",
        "The weather is okay today.",
        "I'm so happy with my purchase!"
    ]
    results = pipeline.run(texts)
    print("\nMultiple texts results:")
    for r in results:
        print(f"Text: {r['text'][:50]}... | Sentiment: {r['sentiment']} | Confidence: {r['confidence']}")
    
    # Example 3: Summary
    summary = pipeline.get_summary(results)
    print(f"\nSummary: {summary}")

if __name__ == "__main__":
    main()
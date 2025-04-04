from mistral_api import ask_mistral

def assess_response_quality():
    quality_metrics = {
        "relevance": 0,
        "coherence": 0,
        "helpfulness": 0
    }
    
    test_query = "Give me tips for LinkedIn profile optimization"
    response = ask_mistral(test_query)
    
    print("Response to analyze:", response)
    print("\nPlease rate the following aspects (1-5):")
    for metric in quality_metrics:
        try:
            score = int(input(f"Rate {metric}: "))
            quality_metrics[metric] = score
        except ValueError:
            print("Invalid input, skipping...")
    
    print("\nQuality Assessment Results:")
    for metric, score in quality_metrics.items():
        print(f"{metric.capitalize()}: {score}/5")

if __name__ == "__main__":
    assess_response_quality()
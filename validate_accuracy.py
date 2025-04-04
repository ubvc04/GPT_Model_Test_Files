from mistral_api import ask_mistral

def validate_accuracy():
    test_cases = [
        {
            "query": "What is LinkedIn?",
            "expected_keywords": ["professional", "network", "platform", "business", "career"]
        },
        {
            "query": "How to write a LinkedIn post?",
            "expected_keywords": ["engagement", "content", "audience", "value", "hashtags"]
        }
    ]
    
    for case in test_cases:
        response = ask_mistral(case["query"])
        found_keywords = sum(1 for keyword in case["expected_keywords"] if keyword.lower() in response.lower())
        accuracy = (found_keywords / len(case["expected_keywords"])) * 100
        
        print(f"\nQuery: {case['query']}")
        print(f"Accuracy: {accuracy}%")
        print(f"Keywords found: {found_keywords}/{len(case['expected_keywords'])}")

if __name__ == "__main__":
    validate_accuracy()
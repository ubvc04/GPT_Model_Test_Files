from mistral_api import ask_mistral
import time

def test_basic_functionality():
    test_cases = [
        "How to improve my LinkedIn profile?",
        "What are best practices for LinkedIn networking?",
        "How to write a good LinkedIn summary?"
    ]
    
    for query in test_cases:
        print(f"\nTesting query: {query}")
        try:
            response = ask_mistral(query)
            print("Response received:", response[:100] + "...")
            time.sleep(1)  # Avoid rate limiting
        except Exception as e:
            print(f"Error for query '{query}': {str(e)}")

if __name__ == "__main__":
    print("Running functional tests...")
    test_basic_functionality()
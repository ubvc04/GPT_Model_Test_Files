from mistral_api import ask_mistral
import time

def validate_mistral_responses():
    validation_tests = [
        {"type": "response_time", "query": "Quick test"},
        {"type": "long_input", "query": "Please analyze my LinkedIn profile..." * 10},
        {"type": "special_chars", "query": "Test with @#$%^&* special characters"}
    ]
    
    for test in validation_tests:
        print(f"\nRunning {test['type']} test")
        start_time = time.time()
        try:
            response = ask_mistral(test["query"])
            duration = time.time() - start_time
            print(f"Response time: {duration:.2f} seconds")
            print(f"Response length: {len(response)} characters")
        except Exception as e:
            print(f"Test failed: {str(e)}")
        time.sleep(1)

if __name__ == "__main__":
    validate_mistral_responses()
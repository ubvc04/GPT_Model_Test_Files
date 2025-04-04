from mistral_api import ask_mistral
import time

def test_consistency():
    test_queries = [
        "How to optimize LinkedIn profile?",
        "Best practices for LinkedIn networking",
        "Tips for LinkedIn content creation"
    ]
    
    iterations = 3
    results = {}

    for query in test_queries:
        print(f"\nTesting consistency for: {query}")
        responses = []
        
        for i in range(iterations):
            try:
                response = ask_mistral(query)
                responses.append(response)
                time.sleep(1)
                
                print(f"Iteration {i+1} complete")
            except Exception as e:
                print(f"Error in iteration {i+1}: {str(e)}")
        
        # Compare responses
        if len(responses) > 1:
            consistency_score = sum(1 for i in range(len(responses)-1)
                                 if responses[i][:100] == responses[i+1][:100])
            print(f"Consistency score: {consistency_score}/{iterations-1}")

if __name__ == "__main__":
    test_consistency()
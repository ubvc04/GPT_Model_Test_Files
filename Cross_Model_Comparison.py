from mistral_api import ask_mistral
import json
import time

def compare_model_responses():
    test_scenarios = [
        {
            "category": "Profile Optimization",
            "query": "How to optimize LinkedIn profile for tech industry?"
        },
        {
            "category": "Content Strategy",
            "query": "What type of content performs best on LinkedIn?"
        },
        {
            "category": "Networking",
            "query": "Best practices for professional networking on LinkedIn?"
        }
    ]
    
    results = {}
    
    for scenario in test_scenarios:
        print(f"\nTesting: {scenario['category']}")
        try:
            # Get response from Mistral
            start_time = time.time()
            mistral_response = ask_mistral(scenario['query'])
            response_time = time.time() - start_time
            
            results[scenario['category']] = {
                "query": scenario['query'],
                "response_time": response_time,
                "response_length": len(mistral_response),
                "preview": mistral_response[:150]
            }
            
            print(f"Response time: {response_time:.2f}s")
            print(f"Response length: {len(mistral_response)} chars")
            print(f"Preview: {mistral_response[:150]}...")
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        time.sleep(1)
    
    # Save comparison results
    with open('model_comparison_results.json', 'w') as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    compare_model_responses()
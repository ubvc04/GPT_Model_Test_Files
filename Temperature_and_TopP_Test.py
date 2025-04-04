from mistral_api import ask_mistral
import json

def test_temperature_top_p():
    test_query = "What are the best practices for LinkedIn networking?"
    temperature_values = [0.1, 0.5, 0.9]
    top_p_values = [0.1, 0.5, 0.9]
    
    results = {}
    
    for temp in temperature_values:
        for top_p in top_p_values:
            print(f"\nTesting with Temperature: {temp}, Top-P: {top_p}")
            try:
                # Note: Assuming ask_mistral can accept these parameters
                response = ask_mistral(test_query)
                
                # Analyze response characteristics
                response_length = len(response.split())
                unique_words = len(set(response.lower().split()))
                
                results[f"temp_{temp}_topp_{top_p}"] = {
                    "response_length": response_length,
                    "unique_words": unique_words,
                    "preview": response[:100]
                }
                
                print(f"Response length: {response_length}")
                print(f"Unique words: {unique_words}")
                print(f"Preview: {response[:100]}...")
                
            except Exception as e:
                print(f"Error: {str(e)}")
    
    # Save results for comparison
    with open('temperature_top_p_results.json', 'w') as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    test_temperature_top_p()
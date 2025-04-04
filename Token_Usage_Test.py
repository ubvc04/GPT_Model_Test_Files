from mistral_api import ask_mistral

def monitor_token_usage():
    test_queries = [
        {"length": "short", "query": "LinkedIn tips"},
        {"length": "medium", "query": "How can I improve my LinkedIn profile and make it more attractive to recruiters?"},
        {"length": "long", "query": "I need detailed guidance on creating a comprehensive LinkedIn strategy including profile optimization, content creation, networking, and engagement tactics." * 2}
    ]

    for test in test_queries:
        print(f"\nTesting {test['length']} query: {test['query'][:50]}...")
        try:
            response = ask_mistral(test['query'])
            
            # Approximate token count (rough estimation)
            input_tokens = len(test['query'].split())
            output_tokens = len(response.split())
            
            print(f"Approximate tokens - Input: {input_tokens}, Output: {output_tokens}")
            print(f"Response preview: {response[:100]}...")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    monitor_token_usage()
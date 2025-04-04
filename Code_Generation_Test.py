from mistral_api import ask_mistral

def test_code_generation():
    code_queries = [
        {
            "scenario": "LinkedIn API Connection",
            "query": "How to connect to LinkedIn API using Python?",
            "expected_elements": ["import", "authentication", "request"]
        },
        {
            "scenario": "Profile Data Extraction",
            "query": "Python script to extract LinkedIn profile data",
            "expected_elements": ["function", "parsing", "data structure"]
        },
        {
            "scenario": "Automated Posting",
            "query": "Code for scheduling LinkedIn posts",
            "expected_elements": ["scheduling", "post creation", "automation"]
        }
    ]

    for test in code_queries:
        print(f"\nTesting {test['scenario']}:")
        try:
            response = ask_mistral(test['query'])
            elements_found = sum(1 for element in test['expected_elements'] 
                               if element.lower() in response.lower())
            
            print(f"Query: {test['query']}")
            print(f"Response preview: {response[:200]}...")
            print(f"Expected elements found: {elements_found}/{len(test['expected_elements'])}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_code_generation()
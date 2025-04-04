from mistral_api import ask_mistral

def test_hallucination():
    factual_queries = [
        {
            "query": "What is LinkedIn's founding date?",
            "known_facts": ["Founded in 2002", "Reid Hoffman", "Mountain View"]
        },
        {
            "query": "What are LinkedIn's premium subscription types?",
            "known_facts": ["Premium Career", "Sales Navigator", "Recruiter Lite"]
        },
        {
            "query": "What is LinkedIn's current user base?",
            "known_facts": ["millions of users", "professional network", "global platform"]
        }
    ]

    for test in factual_queries:
        print(f"\nTesting query: {test['query']}")
        try:
            response = ask_mistral(test['query'])
            fact_matches = sum(1 for fact in test['known_facts'] 
                             if fact.lower() in response.lower())
            
            print(f"Response: {response[:200]}...")
            print(f"Fact verification score: {fact_matches}/{len(test['known_facts'])}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_hallucination()
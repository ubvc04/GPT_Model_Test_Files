from mistral_api import ask_mistral

def run_test_queries():
    test_queries = {
        "profile_optimization": "How to optimize LinkedIn profile?",
        "networking": "Best networking strategies for LinkedIn",
        "content_creation": "Tips for creating engaging LinkedIn content",
        "job_search": "How to use LinkedIn for job search?",
        "engagement": "How to increase LinkedIn post engagement?"
    }
    
    results = {}
    for category, query in test_queries.items():
        print(f"\nTesting {category}...")
        try:
            response = ask_mistral(query)
            results[category] = {
                "status": "success",
                "response_preview": response[:100]
            }
        except Exception as e:
            results[category] = {
                "status": "failed",
                "error": str(e)
            }
    
    print("\nTest Results:")
    for category, result in results.items():
        print(f"\n{category}:")
        print(f"Status: {result['status']}")
        if result['status'] == 'success':
            print(f"Preview: {result['response_preview']}...")

if __name__ == "__main__":
    run_test_queries()
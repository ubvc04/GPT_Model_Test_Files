from mistral_api import ask_mistral

def run_test_scenarios():
    scenarios = [
        {
            "name": "New User Guidance",
            "query": "I'm new to LinkedIn, where should I start?",
            "expected_topics": ["profile setup", "connections", "basic features"]
        },
        {
            "name": "Content Strategy",
            "query": "How to create a content strategy for LinkedIn?",
            "expected_topics": ["posting schedule", "content types", "audience"]
        },
        {
            "name": "Professional Growth",
            "query": "How to use LinkedIn for career growth?",
            "expected_topics": ["networking", "skills", "opportunities"]
        }
    ]
    
    for scenario in scenarios:
        print(f"\nTesting Scenario: {scenario['name']}")
        try:
            response = ask_mistral(scenario["query"])
            print("Response received:")
            print(response[:200] + "...")
            
            topics_found = sum(1 for topic in scenario["expected_topics"] 
                             if any(t.lower() in response.lower() for t in topic.split()))
            
            print(f"Topics covered: {topics_found}/{len(scenario['expected_topics'])}")
        except Exception as e:
            print(f"Scenario failed: {str(e)}")

if __name__ == "__main__":
    run_test_scenarios()
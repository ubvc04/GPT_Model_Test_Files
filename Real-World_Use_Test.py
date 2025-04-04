from mistral_api import ask_mistral
import time

def simulate_real_world_usage():
    user_scenarios = [
        {
            "user_type": "New Graduate",
            "queries": [
                "How to create first LinkedIn profile",
                "How to connect with alumni",
                "Entry level job search on LinkedIn"
            ]
        },
        {
            "user_type": "Career Changer",
            "queries": [
                "Highlight transferable skills on LinkedIn",
                "Network in new industry",
                "Career transition story"
            ]
        },
        {
            "user_type": "Senior Professional",
            "queries": [
                "Executive LinkedIn presence",
                "Thought leadership content",
                "Industry influence building"
            ]
        }
    ]

    for scenario in user_scenarios:
        print(f"\nTesting scenario for: {scenario['user_type']}")
        for query in scenario['queries']:
            try:
                start_time = time.time()
                response = ask_mistral(query)
                duration = time.time() - start_time
                
                print(f"\nQuery: {query}")
                print(f"Response time: {duration:.2f} seconds")
                print(f"Response preview: {response[:150]}...")
                
                time.sleep(1)  # Simulate natural usage pattern
            except Exception as e:
                print(f"Error: {str(e)}")

if __name__ == "__main__":
    simulate_real_world_usage()
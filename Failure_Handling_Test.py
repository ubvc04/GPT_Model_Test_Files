from mistral_api import ask_mistral
import time

def test_failure_handling():
    failure_scenarios = [
        {
            "name": "Network Timeout",
            "test": lambda: time.sleep(10)
        },
        {
            "name": "Invalid Input",
            "test": lambda: ask_mistral(None)
        },
        {
            "name": "Rate Limiting",
            "test": lambda: [ask_mistral("test") for _ in range(5)]
        },
        {
            "name": "Large Response",
            "test": lambda: ask_mistral("Give me a very detailed LinkedIn guide" * 10)
        }
    ]

    for scenario in failure_scenarios:
        print(f"\nTesting: {scenario['name']}")
        try:
            scenario['test']()
            print("Test completed without errors")
        except Exception as e:
            print(f"Error caught: {str(e)}")
            print("Failure handling successful")

if __name__ == "__main__":
    test_failure_handling()
from mistral_api import ask_mistral

def test_edge_cases():
    edge_cases = [
        {
            "name": "Empty Input",
            "input": ""
        },
        {
            "name": "Very Long Input",
            "input": "LinkedIn advice " * 100
        },
        {
            "name": "Special Characters",
            "input": "!@#$%^&*()_+-=[]{}|;:',.<>?"
        },
        {
            "name": "Multiple Languages",
            "input": "LinkedIn 领英 リンクトイン LinkedIn लिंक्डइन"
        },
        {
            "name": "Unicode Characters",
            "input": "LinkedIn™ • ★ ☆ ⚡ ☀ ☂ ☹ ☺"
        }
    ]

    for case in edge_cases:
        print(f"\nTesting: {case['name']}")
        try:
            response = ask_mistral(case['input'])
            print(f"Response received: {response[:100]}...")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_edge_cases()
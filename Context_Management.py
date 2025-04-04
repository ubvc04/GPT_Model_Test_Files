from mistral_api import ask_mistral

def test_context_management():
    conversation_flow = [
        {
            "context": "Initial Query",
            "message": "I want to improve my LinkedIn profile"
        },
        {
            "context": "Follow-up Question",
            "message": "What should I focus on first?"
        },
        {
            "context": "Specific Detail",
            "message": "How should I write my summary?"
        },
        {
            "context": "Related Question",
            "message": "What about my experience section?"
        }
    ]

    for step in conversation_flow:
        print(f"\nTesting {step['context']}:")
        try:
            response = ask_mistral(step['message'])
            print(f"Query: {step['message']}")
            print(f"Response: {response[:150]}...")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_context_management()
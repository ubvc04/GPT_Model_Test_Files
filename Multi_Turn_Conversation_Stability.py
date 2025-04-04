from mistral_api import ask_mistral
import time

def test_conversation_stability():
    conversation_flows = [
        {
            "flow_name": "Profile Development",
            "turns": [
                "I want to improve my LinkedIn profile",
                "What should I focus on first?",
                "How can I improve my summary section?",
                "What about my experience section?",
                "Should I add certifications?"
            ]
        },
        {
            "flow_name": "Content Strategy",
            "turns": [
                "How to create engaging LinkedIn content?",
                "What types of posts work best?",
                "How often should I post?",
                "How can I measure post performance?",
                "What hashtags should I use?"
            ]
        }
    ]

    for flow in conversation_flows:
        print(f"\nTesting conversation flow: {flow['flow_name']}")
        context = []
        
        for i, query in enumerate(flow['turns'], 1):
            try:
                print(f"\nTurn {i}:")
                print(f"Query: {query}")
                
                response = ask_mistral(query)
                context.append(response[:100])  # Store partial context
                
                print(f"Response: {response[:150]}...")
                
                # Check context consistency
                if len(context) > 1:
                    print("Checking context consistency...")
                    for prev_context in context[:-1]:
                        if prev_context.lower() in response.lower():
                            print("✓ Previous context maintained")
                
                time.sleep(1)
                
            except Exception as e:
                print(f"Error in turn {i}: {str(e)}")

if __name__ == "__main__":
    test_conversation_stability()
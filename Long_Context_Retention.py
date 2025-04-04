from mistral_api import ask_mistral
import time

def test_context_retention():
    conversation_chain = [
        {
            "context": "Initial Setup",
            "query": "I want to establish a strong LinkedIn presence for my tech startup"
        },
        {
            "context": "Profile Development",
            "query": "Based on my previous question, what should my profile highlight?"
        },
        {
            "context": "Content Strategy",
            "query": "Considering my startup focus, what content should I post?"
        },
        {
            "context": "Network Building",
            "query": "How should I grow my network in the tech startup space?"
        }
    ]

    context_memory = []
    
    for step in conversation_chain:
        print(f"\nTesting {step['context']}:")
        try:
            response = ask_mistral(step['query'])
            context_memory.append(response[:100])
            
            print(f"Query: {step['query']}")
            print(f"Response: {response[:150]}...")
            
            # Check context retention
            if len(context_memory) > 1:
                print("Context continuity check...")
                for prev_response in context_memory[:-1]:
                    if prev_response.lower() in response.lower():
                        print("✓ Previous context referenced")
            
            time.sleep(1)
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_context_retention()
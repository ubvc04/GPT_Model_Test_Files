from mistral_api import ask_mistral
import time

def test_prompt_variations():
    base_prompts = [
        {
            "intent": "Profile Optimization",
            "variations": [
                "How do I improve my LinkedIn profile?",
                "What makes a LinkedIn profile stand out?",
                "Tips for LinkedIn profile enhancement",
                "Best practices for LinkedIn profile"
            ]
        },
        {
            "intent": "Networking Strategy",
            "variations": [
                "How to network on LinkedIn?",
                "Best LinkedIn networking strategies",
                "Effective LinkedIn connection methods",
                "Professional networking on LinkedIn"
            ]
        }
    ]

    for prompt_set in base_prompts:
        print(f"\nTesting variations for: {prompt_set['intent']}")
        responses = []
        
        for variation in prompt_set['variations']:
            try:
                response = ask_mistral(variation)
                responses.append(response[:100])
                print(f"\nPrompt: {variation}")
                print(f"Response: {response[:100]}...")
                time.sleep(1)
            except Exception as e:
                print(f"Error: {str(e)}")

        # Compare response similarity
        if responses:
            unique_responses = len(set(responses))
            print(f"\nUnique response variations: {unique_responses}/{len(prompt_set['variations'])}")

if __name__ == "__main__":
    test_prompt_variations()
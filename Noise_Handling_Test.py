from mistral_api import ask_mistral

def test_noise_handling():
    noise_test_cases = [
        {
            "type": "Typos",
            "query": "Hwo to improv my linkdin profle?"
        },
        {
            "type": "Extra Spaces",
            "query": "How    to    write    a    good    LinkedIn    summary?"
        },
        {
            "type": "Mixed Case",
            "query": "HoW tO gEt MoRe CoNnEcTiOnS oN lInKeDiN?"
        },
        {
            "type": "Special Characters",
            "query": "L!nked|n pr0f!le opt!m!zat!0n t!ps?"
        }
    ]

    for case in noise_test_cases:
        print(f"\nTesting {case['type']} handling:")
        try:
            response = ask_mistral(case['query'])
            print(f"Noisy query: {case['query']}")
            print(f"Response: {response[:150]}...")
            
            # Check if response is coherent despite noise
            coherence_markers = ["linkedin", "profile", "professional"]
            coherence_score = sum(1 for marker in coherence_markers 
                                if marker in response.lower())
            print(f"Coherence score: {coherence_score}/{len(coherence_markers)}")
            
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_noise_handling()
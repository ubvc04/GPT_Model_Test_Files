from mistral_api import ask_mistral
import re

def test_grammar_fluency():
    test_cases = [
        {
            "complexity": "Simple",
            "query": "How to add skills on LinkedIn?"
        },
        {
            "complexity": "Medium",
            "query": "Explain the best practices for LinkedIn profile optimization considering both visibility and professional presentation."
        },
        {
            "complexity": "Complex",
            "query": "What are the interconnected strategies for building a comprehensive LinkedIn presence while maintaining authenticity and leveraging network effects?"
        }
    ]

    def analyze_response(text):
        sentence_count = len(re.split(r'[.!?]+', text))
        avg_word_length = sum(len(word) for word in text.split()) / len(text.split())
        return {
            "sentence_count": sentence_count,
            "avg_word_length": round(avg_word_length, 2),
            "total_words": len(text.split())
        }

    for case in test_cases:
        print(f"\nTesting {case['complexity']} query:")
        try:
            response = ask_mistral(case['query'])
            metrics = analyze_response(response)
            print(f"Query: {case['query']}")
            print(f"Metrics: {metrics}")
            print(f"Response preview: {response[:150]}...")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_grammar_fluency()
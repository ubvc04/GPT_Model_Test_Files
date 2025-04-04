from mistral_api import ask_mistral

def test_language_support():
    language_tests = [
        {"language": "English", "query": "How to improve LinkedIn profile?"},
        {"language": "Spanish", "query": "¿Cómo mejorar el perfil de LinkedIn?"},
        {"language": "French", "query": "Comment améliorer le profil LinkedIn?"},
        {"language": "German", "query": "Wie verbessere ich das LinkedIn-Profil?"},
        {"language": "Chinese", "query": "如何改善LinkedIn档案？"}
    ]

    for test in language_tests:
        print(f"\nTesting {test['language']} support:")
        try:
            response = ask_mistral(test['query'])
            print(f"Query: {test['query']}")
            print(f"Response preview: {response[:150]}...")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_language_support()
from mistral_api import ask_mistral

def test_mistral_connection():
    try:
        # Test with a simple query
        test_query = "Hello, are you connected?"
        response = ask_mistral(test_query)
        
        if response:
            print("✅ Connection to Mistral API successful!")
            print("Test response:", response)
            return True
    except Exception as e:
        print("❌ Connection to Mistral API failed!")
        print("Error:", str(e))
        return False

if __name__ == "__main__":
    print("\nTesting Mistral API connection...\n")
    test_mistral_connection()
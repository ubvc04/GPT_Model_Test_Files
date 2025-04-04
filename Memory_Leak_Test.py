from mistral_api import ask_mistral
import psutil
import time
import os

def monitor_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # Convert to MB

def test_memory_usage():
    iterations = 50
    memory_usage = []
    test_query = "Give me LinkedIn profile optimization tips"
    
    print("Starting memory leak test...")
    print(f"Initial memory usage: {monitor_memory():.2f} MB")
    
    for i in range(iterations):
        try:
            start_memory = monitor_memory()
            response = ask_mistral(test_query)
            end_memory = monitor_memory()
            
            memory_usage.append(end_memory - start_memory)
            
            print(f"\nIteration {i+1}/{iterations}")
            print(f"Memory delta: {memory_usage[-1]:.2f} MB")
            print(f"Current total memory: {end_memory:.2f} MB")
            
            time.sleep(1)  # Prevent rate limiting
            
        except Exception as e:
            print(f"Error in iteration {i+1}: {str(e)}")
    
    print("\nMemory Test Results:")
    print(f"Average memory delta: {sum(memory_usage)/len(memory_usage):.2f} MB")
    print(f"Max memory spike: {max(memory_usage):.2f} MB")
    print(f"Final memory usage: {monitor_memory():.2f} MB")

if __name__ == "__main__":
    test_memory_usage()
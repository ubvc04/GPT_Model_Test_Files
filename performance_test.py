from mistral_api import ask_mistral
import time
import statistics

def run_performance_test():
    test_query = "Quick LinkedIn tip"
    iterations = 5
    response_times = []
    
    print(f"Running performance test with {iterations} iterations...")
    
    for i in range(iterations):
        start_time = time.time()
        try:
            response = ask_mistral(test_query)
            end_time = time.time()
            response_time = end_time - start_time
            response_times.append(response_time)
            print(f"Iteration {i+1}: {response_time:.2f} seconds")
        except Exception as e:
            print(f"Error in iteration {i+1}: {str(e)}")
        time.sleep(2)
    
    if response_times:
        avg_time = statistics.mean(response_times)
        max_time = max(response_times)
        min_time = min(response_times)
        
        print("\nPerformance Results:")
        print(f"Average response time: {avg_time:.2f} seconds")
        print(f"Maximum response time: {max_time:.2f} seconds")
        print(f"Minimum response time: {min_time:.2f} seconds")

if __name__ == "__main__":
    run_performance_test()
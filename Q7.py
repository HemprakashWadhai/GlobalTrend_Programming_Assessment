#7. Write a Python decorator that measures the execution time of a function and logs it. Apply this decorator to a function that performs a computationally expensive task.
import time
import functools

# Decorator function to measure execution time and log it
def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute")
        return result
    return wrapper

# Memoization decorator for Fibonacci function
def memoize(func):
    memo = {}
    @functools.wraps(func)
    def wrapper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return wrapper

# Example: Recursive Fibonacci function with memoization
@measure_time
@memoize
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
n = 35  # Calculate the 35th Fibonacci number (computationally expensive)
result = fibonacci_recursive(n)
print(f"The {n}th Fibonacci number is: {result}")

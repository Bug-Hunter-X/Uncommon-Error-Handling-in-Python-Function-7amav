def improved_function_with_error_handling(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        raise ValueError("Division by zero!")
    except TypeError as e:
        raise TypeError(f"Type error occurred: {e}")

# improved error handling
try:
    result = improved_function_with_error_handling(10, 0)
    print(result)
except ValueError as e:
    print(f"Caught ValueError: {e}")
try:
    result = improved_function_with_error_handling(10, 'abc')
    print(result)
except TypeError as e:
    print(f"Caught TypeError: {e}")

try:
    result = improved_function_with_error_handling(10, 2)
    print(result) # Output: 5.0
except Exception as e:
    print(f"An unexpected error occurred: {e}")
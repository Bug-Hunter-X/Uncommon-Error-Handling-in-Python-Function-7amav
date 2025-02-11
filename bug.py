def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        return None

# This will cause an unexpected behavior
result = function_with_uncommon_error(10, 0)
print(result)  # Output: inf
result = function_with_uncommon_error(10, 'abc')
print(result)  # Output: None
result = function_with_uncommon_error(10, 2)
print(result) # Output: 5.0
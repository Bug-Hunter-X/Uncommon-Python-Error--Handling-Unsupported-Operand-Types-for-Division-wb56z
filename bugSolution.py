def improved_function_with_type_checking(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Inputs must be numbers"
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Example usage
print(improved_function_with_type_checking(10, 2))  # Output: 5.0
print(improved_function_with_type_checking(10, 0))  # Output: Error: Division by zero
print(improved_function_with_type_checking(10, "hello")) # Output: Error: Inputs must be numbers
print(improved_function_with_type_checking(10, [1,2])) # Output: Error: Inputs must be numbers
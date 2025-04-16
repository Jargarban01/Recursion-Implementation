def sum_of_digits(n):
    # Base case: if n is a single digit (0-9), return n
    if n < 10:
        return n
    
    # Recursive case: sum the last digit (n % 10) and the sum of digits of the remaining number (n // 10)
    return (n % 10) + sum_of_digits(n // 10)

# Example usage
numbers = [1234, 567, 0, 9999]
for num in numbers:
    result = sum_of_digits(num)
    print(f"Sum of digits in {num} = {result}")

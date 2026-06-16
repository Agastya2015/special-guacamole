number = int(input("Enter a decimal number: "))
print("Binary: {decimal_to_binary(number)}")

def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary  # Prepend to keep correct order
        n = n // 2
    return binary



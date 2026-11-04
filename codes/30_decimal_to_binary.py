def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Negative numbers not allowed")
    if number == 0:
        return "0"
    binary = ""
    n = number
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary
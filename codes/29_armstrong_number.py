def is_armstrong(number):
    if number < 0:
        return False
    s = str(number)
    power = len(s)
    total = sum(int(digit) ** power for digit in s)
    return total == number
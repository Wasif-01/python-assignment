def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total

num = int(input("Enter a number: "))
result = sum_digits(num)
print("Sum of digits =", result)

def is_palindrome(number):
    number = str(number)
    middle = len(number) // 2
    for i in range(middle):
        if number[i] != number[-i - 1]:
            return False
    return True

result1 = is_palindrome(123321)
result2 = is_palindrome(123456)
print(result1)
print(result2)
def print_odd_numbers(start, end):
    if start % 2 == 0:
        start += 1
    for num in range(start, end + 1, 2):
        print(num)
print_odd_numbers(1, 55)
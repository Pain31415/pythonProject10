def sum_in_range(start, end):
    sum = 0
    for i in range(start, end):
        sum += i
    return sum
sum = sum_in_range(15, 50)
print(f"Сума чисел в діапазоні: {sum}")
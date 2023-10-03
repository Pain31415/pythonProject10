def product_in_range(start, end):
    if start > end:
        start, end = end, start
    product = 1
    for number in range(start, end + 1):
        product *= number
    return product
result = product_in_range(5, 25)
print("Добуток чисел у діапазоні:", result)
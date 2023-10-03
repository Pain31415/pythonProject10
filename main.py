def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
user_input = input("Введіть число для перевірки, чи воно є простим: ")
try:
    user_number = int(user_input)
    result = is_prime(user_number)
    if result:
        print(f"{user_number} є простим числом.")
    else:
        print(f"{user_number} не є простим числом.")
except ValueError:
    print("Введено нечислове значення. Будь ласка, введіть ціле число.")
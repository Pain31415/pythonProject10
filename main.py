def is_lucky_number(number):
    if len(str(number)) != 6:
        return False
    digits = [int(digit) for digit in str(number)]
    if sum(digits[:3]) == sum(digits[3:]):
        return True
    else:
        return False
user_input = input("Введіть шестизначне число для перевірки, чи воно є 'щасливим': ")
try:
    user_number = int(user_input)
    if is_lucky_number(user_number):
        print(f"{user_number} є щасливим числом.")
    else:
        print(f"{user_number} не є щасливим числом.")
except ValueError:
    print("Введено невірне значення. Будь ласка, введіть шестизначне число.")
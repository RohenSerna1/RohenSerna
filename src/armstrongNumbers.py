def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number

num = int(input("Ingrese un numero: "))
if is_armstrong(num):
    print(f"{num} es Armstrong")
else:
    print(f"{num} no es Armstrong")
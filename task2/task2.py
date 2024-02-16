import re
from typing import Callable

def generator_numbers(text: str):

    pattern= r'\b\d+\.\d+\b|\b\d+\b'

    numbers = re.findall(pattern, text) # шукаємо всі числа
    
    for number in numbers:
        yield float(number) # повертаємо на кожний ітерації число(генератор).


def sum_profit(text:str,func:Callable):
    total_sum = sum(func(text)) # sum вбудована функція, яка приймає ітерабельний об'єкт

    return total_sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


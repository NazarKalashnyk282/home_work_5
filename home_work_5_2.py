import re
from typing import Callable

def generator_numbers(text: str):
    # Регулярний вираз для пошуку дійсних чисел
    pattern = r'\b\d+\.\d+\b|\b\d+\b'
    
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Повертаємо числа як дійсні числа

def sum_profit(text: str, func: Callable):
    total_sum = sum(func(number) for number in generator_numbers(text))
    return total_sum



text_example = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_profit = sum_profit(text_example, func=lambda x: x)
print(f"Загальний прибуток: {total_profit:.2f}")
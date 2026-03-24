# 1. Напиши код который выведет таблицу умножения до 10 на N (введенное с клавиатуры) в таком формате
#   3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27

def output_table(n: int):
    for i in range(1, 10):
        print(n * i, end="")
        if i != 9:
            print(' | ', end="")


print(int(input('Введите число N ')))
output_table(3)



# 2. Попроси пользователя ввести имя и возраст. Выведи фразу: «Через 10 лет тебе будет <X> лет, <ИМЯ>!»

name = input("Введите имя:")
age = int(input("Введите возраст:"))

output_age: int = age + 10

print(f"Через 10 лет тебе будет {output_age} лет, {name}!")



# 3. Даны два списка цен в долларах и курс валюты. Используй map чтобы перевести все цены в рубли. Затем используй zip чтобы создать словарь {товар: цена_в_рублях}:


items = ["хлеб", "молоко", "кофе"]
prices_usd = [1.5, 2.0, 8.0]
rate = 3.2


def to_conversion(price: float):
    return price * rate


prices = list(map(to_conversion, prices_usd))
prices_dict = dict(zip(items, prices))

print(prices_dict)



# 4.Напиши функцию fizzbuzz(n) которая принимает число и возвращает строку: 'Fizz' если делится на 3, 'Buzz' если делится на 5, 'FizzBuzz' если делится на оба, иначе само число в виде строки. Вызови её для чисел от 1 до 20 через map.

def fizzbuzz(n: int):
    if n % 3 == 0:
       return "Fizz"

    if n % 5 == 0:
        return "Buzz"

    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    else:
        return str(n)
    
result = list(map(fizzbuzz, range(1, 21)) )
print(result)



# 5. Напиши функцию *args с именем my_stats которая принимает любое количество чисел и возвращает сразу три значения — минимум, максимум и среднее.

def my_stats(first: int, *args: tuple):
    numbers = (first,) + args
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

print(my_stats(5, 2, 8, 1, 9))   




# 6. Напиши функцию build_profile(**kwargs) которая принимает любые именованные аргументы и возвращает словарь с этими данными плюс автоматически добавляет ключ 'registered': True. Добавь к функции docstring.

def build_profile(**kwargs):
    profile = dict(kwargs)
    profile['registered'] = True
    return profile

user = build_profile(name="Alex", age=30, city="Minsk")
print(user)




# 7. Создай модуль math_utils.py с тремя функциями: square(n) — возводит в квадрат, cube(n) — возводит в куб, is_even(n) — возвращает True/False. В main.py импортируй модуль, попроси пользователя ввести число через input, примени все три функции и выведи результаты. Защити вызовы конструкцией if __name__ == "__main__".

import math_utils

def main():
    num = int(input("Введите число: "))

    print("Квадрат:", math_utils.squaren(num))
    print("Куб:", math_utils.cub(num))
    print("Четное?:", math_utils.is_iven(num))


if __name__ == "__main__":
    main()

            


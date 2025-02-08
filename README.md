За эти 30 дней я попытаюсь написать полностью работающий калькулятор на Python с нуля! 
Сегодня начнется мое обучние базе и азам Python!
Прошло примерно 1,5 часа моего обучения. Моей отправной точкой стал код простого калькулятора который принимает только 2 числа,имея функции умножения деления вычетания и прибавления.Из специфичного только квадратный корень.По мере данного челленджа я обираюсь его модифицировать и создать что то на подобии тетриса используя видеоматериалы.
import math

print("Welcome to calculator! Print your numbers,for now only 2 numbers")
print("Here is the list of commands: Sum, square_root,subtraction,multiply,divide")
a = int(input())
b = int(input())
user_input = input()
if user_input == "sum":
    print(a + b)
elif user_input == "square_root":
    print(math.sqrt(a + b))
elif user_input == "subtraction":
    print(a - b)
elif user_input == "multiply":
    print(a * b)
elif user_input == "divide":
    print(a / b)

  Вот в чем весь мой код,надеюсь за этот челлендж я пойму как писать более сложные функции и даже программы на примере калькулятора и тетриса.Это будет увлекательное изучение пайтона!

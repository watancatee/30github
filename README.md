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

  Вот в чем весь мой код,надеюсь за этот челлендж я пойму как писать более сложные функции и даже программы на примере калькулятора и тетриса.Это будет увлекательное изучение пайтона

  Сегодня 2 день челленджа 30github и я продолжу настройку своего калькулятора
  В этот день я начну исправление того чтобы пользователь мог вводить не только 2 числа.
  Мне пришлось польностью переосмыслить свой код чтобы попытаться исправить данный недочет.К сожалению спрашивая у чата,он дает только код без нормального обьяснения и поэтому я буду смотреть видеоролики на Youtube для более целостносного погружения.Действия команд которые я узнал

  for num in numbers(numbers - список) - проходится по всем числам в списке,используется в вычитании делении умножении
  if len(numbers) - проверка пустой список или нет
  lower() - читает все символы как строчные,так что не будет ошибки когда введешь команду с строчными буквами

  Завтра я попытаюсь наконец таки написать свой полностью работающий калькулятор!


  Сегодня я продолжил работу над  собственным калькулятором.

К сожалению, сегодня я не смог завершить работу над кодом, так как столкнулся с некоторыми трудностями в логике обработки операций. Но помимо этого я изучил новые функции в пайтоне и вот какие:


map(int, input().split()) – позволяет преобразовать введённые пользователем данные в список чисел.

sum(numbers) – удобный способ сложить все числа в списке.

math.prod(numbers) – полезная функция для вычисления произведения всех чисел.

План на завтра:

Завтра я постараюсь окончательно реализовать основные математические операции и протестировать работу калькулятора.



Сегодня уже 4 день с началачеленджа от гитхаб,и я продолжаю изучать разлчиные функции в пайтоне чтобы написать свой собственный калькулятор.Из за того что я пишу такие коды впервые то мне тяжело проудумывать логику действий у этого калькулятора.Вот некоторые функции которые я изучил и их применение:

min() - находит минимальное число из списка
abs() - возвращает абсолютное значение числа
max() - находит максимальное число из списка
pow() - возводит в степень заданное число

На изучении функции и завершается мой день,буду даьше изучать различные функции и потом настраивать логику калькулятора с помощью них



Сегодня 5 день челленджа от growthungry  и я также продолжаю создание своего калькулятора.Помимо изуения различных функций для полноценного калькулятора я также параллельно начал смотреть различные курсы,читать другие текстовые источники или записи о пайтоне.Список функций и их использование:
def safe_divide(a, b):
    return a / b if b != 0 else "Ошибка" - определяет является ли число нулем если оно делится,и если это так то выводит ошибку в консоль
    abs() – модуль числа
    enumerate() – нумерация элементов в списке
На сегодняшний день это все функции которые я изучил,и с времнным осмыслением логики моего калькулятора я также буду изучать вообщем функции пайтона отдельные от математики!




Сегодня 6 день челленджа от growthhungry и я продолжаю изучение пайтона,и попытки написания калькулятора на нем.
ast.literal_eval() - безопасное вычисление выражений,и наверное мини калькулятор
math.log() - логарифм в математике
math.fsum() - работает точнее чем обычный sum()

Также вот некоторый список функции который не связан с куалькулятором но есть в пайтоне:
time.sleep() - пауза в выполнении кода,довольно полезно в будущих проектах
datetime.now() - вычисляет текущую дату 
sorted() - сортировка списка в порядке возрастания

Пайтон это очень увлекательный язык,и я продолжу его изучение даже после 30 дней челленджа!


Сегодня 7 день челленджа от growthhungry, и я продолжаю изучение Python, а также работу над  калькулятором.

Новые полезные функции для калькулятора:
 eval() – выполняет строку как код, но использовать осторожно из-за безопасности.
 round(число, знаки) – округляет число до нужного количества знаков после запятой.
 abs(число) – модуль числа (превращает отрицательное число в положительное).

Дополнительные функции в Python:
 time.time() – возвращает текущее время в секундах с начала эпохи (полезно для замеров).
 datetime.strftime() – форматирует дату в удобный строковый вид.
 reversed(список) – переворачивает последовательность без изменения оригинала.

 very soon
 nah
 no chance
 I GOT IT
 finally
 soon enough for challenge to be compleete
why
yup
# GITHUB 30 CHALLENGE
git add
git commit
git push origin main

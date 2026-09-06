import sys
a = 0
b = 0
c = 1
d = 0
def func():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input('''
Напишите номер команды:
1. Сложение
2. Вычитание
3. Умножение
4. Деление
5. Возведение в степень
0. Выход
-- '''))
    if c == 1:
        d = a+b
        print("Итог "+str(d))
    if c == 2:
        d = a-b
        print("Итог "+str(d))
    if c == 3:
        d = a*b
        print("Итог "+str(d))
    if c == 4:
        d = a/b
        print("Итог "+str(d))
    if c == 5:
        d = a**b
        print("Итог "+str(d))
    elif c == 0:
        print("До свидания")
        sys.exit(0)
    return
while c != 0:
    func()

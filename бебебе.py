import sys
import msvcrt
import os
a = 0
b = 0
c = 1
d = 0
def conclear():
    os.system('cls' if os.name == 'nt' else 'clear')
def enter_check():
    char = msvcrt.getch()
    if char in (b'\r', b'\n'):
        return True
    return False
def func():
    conclear()
    a = int(input('''
Введите первое число: '''))
    conclear()
    b = int(input("Введите второе число: "))
    conclear()
    c = int(input('''
======================
Напишите номер команды:
======================
1| Сложение
2| Вычитание
3| Умножение
4| Деление
5| Возведение в степень
0| Выход
-- '''))
    if c == 1:
        d = a+b
        print('''
===============
    Итог '''+str(d))
        print("===============")
    if c == 2:
        d = a-b
        print('''
===============
    Итог '''+str(d))
        print("===============")
    if c == 3:
        d = a*b
        print('''
===============
    Итог '''+str(d))
        print("===============")
    if c == 4:
        if b != 0:
            d = a/b
            print('''
    ===============
        Итог '''+str(d))
            print("===============")
        else:
            print("Ошибка: на ноль делить нельзя!")
    if c == 5:
        d = a**b
        print('''
===============
    Итог '''+str(d))
        print("===============")
    elif c == 0:
        print('''
До свидания!''')
        sys.exit(0)
    
    print("\nНажмите Enter, чтобы продолжить...")
    if enter_check():
        conclear()
    return
while c != 0:
    func()


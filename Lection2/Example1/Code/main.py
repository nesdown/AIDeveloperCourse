# isFunctionHeroCodePython - Camel Case (Верблюжий ввод)
# is_function_hero_code_python - Snake Case (Змеиный ввод)

#Импортируем модуль System (System = sys)
import sys
import time as MyTime

try:
    number1 = int(input("Введите первое число: "))
    #time.sleep(5)
    MyTime.sleep(5)
    number2 = int(input("Введите второе число: "))

except Exception:
    print("Что-то пошло не так.")
    sys.exit()

def isDividable(x, y):
    if (x % y == 0):
        return "Число 1 делится на число 2 без остатка."
    else:
        return "Число 1 не делится на число 2 без остатка."

print(isDividable(number1, number2))
    # int('Stroka') - строку в число
    # str(14) - число в строку

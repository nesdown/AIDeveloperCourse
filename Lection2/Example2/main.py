# dictionary "Словарь русско-английский"

def getTranslation(word):
  if (word == 'кот'):
    return 'cat'
  elif (word == 'стол'):
    return 'table'
  elif (word == 'ручка'):
    return 'pen'
  elif (word == 'телефон'):
    return 'phone'
  elif (word == 'часы'):
    return 'clock'
  elif (word == 'бумага'):
    return 'paper'
  elif (word == 'линза'):
    return 'lens'
  elif (word == 'зеркало'):
    return 'mirror'
  elif (word == 'призма'):
    return 'prism'
  elif (word == 'робот'):
    return 'robot'


result1 = getNumber('кот')
result2 = getNumber('стол')
result3 = getNumber('ручка')
result4 = getNumber('телефон')
result5 = getNumber('часы')
result6 = getNumber('бумага')
result7 = getNumber('линза')
result8 = getNumber('зеркало')
result9 = getNumber('призма')
result10 = getNumber('робот')


print (
    'кот' + ' '+ str (getNumber('кот')) + '\n'  +
    'стол ' + str () + '\n' + 'ручка' + ' '+
    str (result3) + '\n'  + 'телефон' + ' '+ str (result4) + '\n'
    + 'часы' + ' '+ str (result5) + '\n'  + 'бумага' + ' '+ str (result6) +
    '\n'  + 'линза' + ' '+ str (result7) + '\n'  + 'зеркало' + ' '+ str (result8) 
    + '\n'  + 'призма' + ' '+ str (result9) + '\n' + 'робот' + ' '+ str (result10)
)


# функция, которая проверяет, делится ли число на 3
def isOdd(number):
  if (number % 3 == 0):
    return 'Это число делится на 3'
  else:
    return 'Это число не делится на три без остатка'
result1 = isOdd(9)
result2 = isOdd(5)
print('isOdd(9)' + ' ' + str (result1) + '\n' + 'isOdd(5)' + ' ' + str (result2))

# Приветствие с таймером
import time
print('Hello!')
time.sleep(1)
print('How are you?')
time.sleep(2)
print('I am fine, thanks')

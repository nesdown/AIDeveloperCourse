import math
from tkinter import *

root = Tk()

calc = StringVar()
calc.set("")

label = Label(textvariable=calc, font="Arial, 16", background='#000', foreground='#fff')

values = []

def onePressed():
  global calc
  calc.set(calc.get() + "1")

def twoPressed():
  global calc
  calc.set(calc.get() + "2")

def threePressed():
  global calc
  calc.set(calc.get() + "3")

def fourPressed():
  global calc
  calc.set(calc.get() + "4")

def fivePressed():
  global calc
  calc.set(calc.get() + "5")

def sixPressed():
  global calc
  calc.set(calc.get() + "6")

def sevenPressed():
  global calc
  calc.set(calc.get() + "7")

def eightPressed():
  global calc
  calc.set(calc.get() + "8")

def ninePressed():
  global calc
  calc.set(calc.get() + "9")

def zeroPressed():
  global calc
  calc.set(calc.get() + "0")

def plusPressed():
  global values
  global calc
  if calc.get() != '':
    values.append(float(calc.get()))
  calc.set("")
  values.append('+')

def minusPressed():
  global values
  global calc
  if calc.get() != '':
    values.append(float(calc.get()))
  calc.set("")
  values.append('-')

def multiplyPressed():
  global values
  global calc
  if calc.get() != '':
    values.append(float(calc.get()))
  calc.set("")
  values.append('*')

def dividePressed():
  global values
  global calc
  if calc.get() != '':
    values.append(float(calc.get()))
  calc.set("")
  values.append('/')

def equalPressed():
  global values
  global calc
  var1 = values[0]
  var2 = 0
  operat = values[1]
  print(operat + '\n' + str(len(values)))

  for i in range(2, len(values) - 1):
    print(i)
    if i % 2 == 0:
      if operat == '+':
        var1 = var1 + values[i]
        print(values[i])
        print(var1)

      elif operat == '-':
        var1 = var1 - values[i]

      elif operat == '/':
        var1 = var1 / values[i]

      elif operat == '*':
        var1 = var1 * values[i]

    else:
      operat = values[i+1]

  calc.set(str(var1))

def createWindow():
  global root
  global label
  root.title("Калькулятор")
  root.geometry("200x450")


  buttons_number = [
    Button(text='1', font='Arial, 36', command=onePressed),
    Button(text='2', font='Arial, 36', command=twoPressed),
    Button(text='3', font='Arial, 36', command=threePressed),
    Button(text='4', font='Arial, 36', command=fourPressed),
    Button(text='5', font='Arial, 36', command=fivePressed),
    Button(text='6', font='Arial, 36', command=sixPressed),
    Button(text='7', font='Arial, 36', command=sevenPressed),
    Button(text='8', font='Arial, 36', command=eightPressed),
    Button(text='9', font='Arial, 36', command=ninePressed),
    Button(text='0', font='Arial, 36', command=zeroPressed)
  ]

  buttons_operators = [
    Button(text='*', font='Arial, 36', command=multiplyPressed),
    Button(text='/', font='Arial, 36', command=dividePressed),
    Button(text='-', font='Arial, 36', command=minusPressed),
    Button(text='+', font='Arial, 36', command=plusPressed)
  ]

  buttons_function = [
    Button(text='=', font='Arial, 36', command=equalPressed),
    Button(text='C', font='Arial, 36')
  ]

  label.grid(row=0, column=0, columnspan=4)

  buttons_number[0].grid(row=1, column=0, sticky="ew")
  buttons_number[1].grid(row=1, column=1, sticky="ew")
  buttons_number[2].grid(row=1, column=2, sticky="ew")
  buttons_number[3].grid(row=2, column=0, sticky="ew")
  buttons_number[4].grid(row=2, column=1, sticky="ew")
  buttons_number[5].grid(row=2, column=2, sticky="ew")
  buttons_number[6].grid(row=3, column=0, sticky="ew")
  buttons_number[7].grid(row=3, column=1, sticky="ew")
  buttons_number[8].grid(row=3, column=2, sticky="ew")
  buttons_number[9].grid(row=4, column=2, sticky="ew")

  buttons_operators[0].grid(row=4, column=0, sticky="ew")
  buttons_operators[1].grid(row=4, column=1, sticky="ew")
  buttons_operators[2].grid(row=5, column=0, sticky="ew")
  buttons_operators[3].grid(row=5, column=1, sticky="ew")

  buttons_function[0].grid(row=5, column=2, sticky="ew")
  buttons_function[1].grid(row=6, column=1, sticky="ew")


  root.mainloop()



createWindow()

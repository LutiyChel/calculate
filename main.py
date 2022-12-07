n1 = int(input("Введите первое число:"))
n2 = int(input("Введите второе число:"))
sign = input("Введите знак операции:")

if sign == "+":
   res = n1 + n2
elif sign == "-":
   res = n1 - n2
elif sign == "/":
  res = n1 / n2
elif sign == "**":
  res = n1 ** n2
else:
  print("Неверный знак!!!")
  
print("Результат = ", res)

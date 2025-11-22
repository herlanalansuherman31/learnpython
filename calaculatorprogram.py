print("====================kalkulator sederhana=========================")
operator = input("masukan operator (+ - * /)= ")
num1 = float(input("masukan nomor pertama= "))
num2 = float(input("masukan nomor kedua= "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print(f"{operator} bukan operator")


# simple_calculator
num1 = input("Please input your first number: ");
op = input("Input the operation you would like to use: ");
num2 = input("Please input your second number: ");
if op == "+":
  print(int(num1)+int(num2))
elif op == "-":
  print(int(num1)-int(num2))
elif op == "*":
  print(int(num1)*int(num2))
elif op == "/":
  print(int(num1)/int(num2))
else:
  print("Invalid operator")


number = int(input("Introduce tu numero: "))
number_2 = int(input("Introduce tu segundo numero: "))
operation = input("Introduce tu operacion (+ - * / pot): ")

if operation == "+":
    print(number + number_2)
elif operation == "-":
    print(number - number_2)
elif operation == "*":
    print(number * number_2)
elif operation == "/":
    print(number / number_2)
elif operation == "pot":
    print(number ** number_2)
else:
    print("El operacion no existe")
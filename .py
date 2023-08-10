def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x // y

print('*****Pyton Calculator*****')

print("\nSelecione o número da opção desejada: \n")

print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")

opção = int(input("\nDigite sua opção (1/2/3/4): "))

if opção <= 0  > 4:
    print("\nOpção inválida!\n")
    exit(0)

num1 = int(input("\nDigite o primeiro termo: "))
num2 = int(input("\nDigite o segundo número: "))
if opção == 1:
    print(num1, "+", num2, "=", addition(num1, num2))
      
elif opção == 2:
    print(num1, "-",num2, "=",subtraction(num1, num2))

elif opção == 3:
    print(num1, "*", num2, "=", multiplication(num1, num2))

elif opção == 4:
    print(num1, "/", num2, "=", division(num1, num2))
    
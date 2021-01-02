from time import sleep
print("=-=-=" * 10)
print("\033[32mPython Calculator\033[m".center(50))
print("=-=-=" * 10)

def add(x=0, y=0):
	return x + y

def sub(x=0, y=0):
	return x - y

def mul(x=0, y=0):
	return x * y

def div(x=0, y=0):
	return x / y

try:
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    while True:
        cal = int(input('''	Escolha uma operação:
        [1] - Adição;
        [2] - Subtração;
        [3] - Multiplicação;
        [4]- Divisão;
        [5]- Sair;
        >>> '''))
        print(f"Você escolheu a opção: {cal}")
        sleep(0.5)
        print("=-=-=" * 10)
        if cal == 1:
            print(f'{num1} + {num2} = ',add(num1, num2))
            print("=-=-=" * 10)
            sleep(1.0)
        elif cal == 2:
            print(f'{num1} x {num2} = ',mul(num1, num2))
            print("=-=-=" * 10)
            sleep(1.0)
        elif cal == 3:
            print(f'{num1} - {num2} = ',sub(num1, num2))
            print("=-=-=" * 10)
            sleep(1.0)
        elif cal == 4:
            print(f'{num1} / {num2} = ',div(num1,num2))
            print("=-=-=" * 10)
            sleep(1.0)
        elif cal == 5:
            print("Volte sempre!!!")
            break
        else:
            print(f"\033[31mPor favor escolha uma opção válida\033[m")
            print("=-=-=" * 10)
    print("=-=-=" * 10)
except:
    print("Ops houve algum erro pf verifique seu código")

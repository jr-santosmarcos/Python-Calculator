print("Python Calculator")

# Escolha dos números e do sinal da operação
num_1 = float(input("Digite o primeiro número: "))
signal = input("Escolha a operação desejada:\n+ | Soma\n- | Subtração\n* | Multiplicação\n/ | Divisão\n")
num_2 = float(input("Digite o segundo número: "))

# Definindo a Classe Calculator
class Calculator():

    # Expressões lambda para cada operação matemática
    add = lambda x, y: x + y
    subtract = lambda x, y: x - y
    multiply = lambda x, y: x * y
    divide = lambda x, y: x / y

    # Função Result para retornar o valor de acordo com a escolha dos números e o sinal da operação
    def Result(x, y):
        if signal == "+":
            result = Calculator.add(x, y)
        elif signal == "-":
            result = Calculator.subtract(x, y)
        elif signal == "*":
            result = Calculator.multiply(x, y)
        else:
            result = Calculator.divide(x, y)
        return result

# Printa na tela a operação e o resultado final
print(f"{num_1} {signal} {num_2} = {Calculator.Result(num_1, num_2)}")
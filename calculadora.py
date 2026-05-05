def somar(x, y): return x + y
def subtrair(x, y): return x - y
def multiplicar(x, y): return x * y
def dividir(x, y): 
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

print("--- Calculadora Python ---")
print("Escolha a operação: \n1.Soma \n2.Subtração \n3.Multiplicação \n4.Divisão \n0.Sair")

while True:
    escolha = input("\nDigite o número da operação: ")

    if escolha == '0':
        print("Saindo... Até logo!")
        break

    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {somar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
    else:
        print("Opção inválida, tente novamente.")
def soma(a, b): return a + b
def subtracao(a, b): return a - b
def multiplicacao(a, b): return a * b
def divisao(a, b):
    if b == 0:
        return "Erro (divisão por zero)"
    return a / b

def calculadora():
    try:
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        
        print("\n Resultado")
        print(f"Soma: {soma(num1, num2)}")
        print(f"Subtração: {subtracao(num1, num2)}")
        print(f"Multiplicação: {multiplicacao(num1, num2)}")
        print(f"Divisão: {divisao(num1, num2)}")
        
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos (use ponto em vez de vírgula).")

if __name__ == "__main__":
    calculadora()

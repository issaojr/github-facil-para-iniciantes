# contador.py
def contar_ate(n):
    for i in range(1, n + 1):
        print(i)

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número para contar até ele: "))
        contar_ate(numero)
    except ValueError:
        print("Por favor, digite um número inteiro.")

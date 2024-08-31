import math

def bem_vindo():
    print("Calculadora de Bhaskara")

def coleta_de_dados():
    a = float(input("Informe o coeficiente a: "))
    b = float(input("Informe o coeficiente b: "))
    c = float(input("Informe o coeficiente c: "))

    print(f"{a}x²+{b}x+{c}")
    return (a, b, c)

def calcule_bhaskara(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Não existem raizes reias")
    elif delta == 0:
        raizes = -b / (2*a)
        print("Existem apenas uma raiz real: {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Ezitem duas raizes reais: {raiz1} e {raiz2}")

bem_vindo()
a, b, c = coleta_de_dados()
calcule_bhaskara(a, b, c)

from src.modulo_1 import mcd_euclides

def main():
    print("Bienvenido al programa para calcular el MCD de dos números.")
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        resultado = mcd_euclides(num1, num2)
        print(f"El Máximo Común Divisor de {num1} y {num2} es: {resultado}")
    except ValueError:
        print("Por favor, ingresa números enteros válidos.")

if __name__ == "__main__":
    main()

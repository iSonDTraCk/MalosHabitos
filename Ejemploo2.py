def calcular_producto_y_suma(factor1, factor2, sumando):

    resultado = factor1 * factor2 + sumando
    return resultado

def main():
    factor1 = float(input("Ingrese el primer factor: "))
    factor2 = float(input("Ingrese el segundo factor: "))
    sumando = float(input("Ingrese el valor a sumar: "))

    resultado = calcular_producto_y_suma(factor1, factor2, sumando)
    print(f"El resultado de {factor1} * {factor2} + {sumando} es: {resultado}")

if __name__ == "__main__":
    main()

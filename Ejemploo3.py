# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(largo, ancho):
    area = largo * ancho
    return area

def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

def main():
    print("Ingrese las dimensiones del rectángulo:")
    largo_rectangulo = float(input("Largo del rectángulo: "))
    ancho_rectangulo = float(input("Ancho del rectángulo: "))
    area_rectangulo = calcular_area_rectangulo(largo_rectangulo, ancho_rectangulo)
    print(f"Área del rectángulo con largo {largo_rectangulo} y ancho {ancho_rectangulo} es: {area_rectangulo}")
    print("\nIngrese las dimensiones del triángulo:")
    base_triangulo = float(input("Base del triángulo: "))
    altura_triangulo = float(input("Altura del triángulo: "))
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print(f"Área del triángulo con base {base_triangulo} y altura {altura_triangulo} es: {area_triangulo}")

if __name__ == "__main__":
    main()

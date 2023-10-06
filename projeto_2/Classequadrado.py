# Função para calcular a área e o perímetro de um quadrado
def calcular_quadrado():
    lado = float(input("Digite o valor do lado do quadrado: "))

    # Função para calcular a área do quadrado
    def area_quadrado():
        area = lado * lado
        return area

    # Função para calcular o perímetro do quadrado
    def perimetro_quadrado():
        perimetro = 4 * lado
        return perimetro

    area = area_quadrado()
    perimetro = perimetro_quadrado()

    print(f"A área do quadrado é: {area}")
    print(f"O perímetro do quadrado é: {perimetro}")
# Função para calcular a área e o perímetro de um triângulo
def calcular_triangulo():
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))
    lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
    lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
    lado3 = float(input("Digite o valor do terceiro lado do triângulo: "))

    # Função para calcular a área do triângulo
    def area_triangulo():
        area = (base * altura) / 2
        return area

    # Função para calcular o perímetro do triângulo
    def perimetro_triangulo():
        perimetro = lado1 + lado2 + lado3
        return perimetro

    area = area_triangulo()
    perimetro = perimetro_triangulo()

    print(f"A área do triângulo é: {area}")
    print(f"O perímetro do triângulo é: {perimetro}")
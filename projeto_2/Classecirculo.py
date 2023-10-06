import math

# Função para calcular a área e o perímetro de um círculo
def calcular_circulo():
    pi = 3.14
    raio = float(input("Digite o raio do círculo: "))

    # Função para calcular a área do círculo
    def area_circulo():
        area = pi * (raio ** 2)
        return area

    # Função para calcular o perímetro do círculo
    def perimetro_circulo():
        perimetro = 2 * pi * raio
        return perimetro

    area = area_circulo()
    perimetro = perimetro_circulo()

    print(f"A área do círculo é: {area}")
    print(f"O perímetro do círculo é: {perimetro}")

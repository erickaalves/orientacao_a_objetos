# Função para calcular a área e o volume de um cubo
def calcular_cubo():
    lado = float(input("Digite o valor do lado do cubo: "))

    # Função para calcular a área do cubo
    def area_cubo():
        area = 6 * (lado ** 2)
        return area

    # Função para calcular o volume do cubo
    def volume_cubo():
        volume = lado ** 3
        return volume

    area = area_cubo()
    volume = volume_cubo()

    print(f"A área do cubo é: {area}")
    print(f"O volume do cubo é: {volume}")

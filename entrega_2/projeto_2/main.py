# Função principal que chama as funções de cálculo com base na escolha do usuário
def main():
    while True:
        print("Escolha uma opção:")
        print("1. Calcular área e perímetro de um círculo")
        print("2. Calcular área e volume de um cubo")
        print("3. Calcular área e perímetro de um quadrado")
        print("4. Calcular área e perímetro de um triângulo")
        print("5. Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            calcular_circulo()
        elif opcao == 2:
            calcular_cubo()
        elif opcao == 3:
            calcular_quadrado()
        elif opcao == 4:
            calcular_triangulo()
        elif opcao == 5:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
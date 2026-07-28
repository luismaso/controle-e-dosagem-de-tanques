opcaomenu = ""

def coletar_ph_tanques(linhas, colunas):
    matriz = []

    for i in range(linhas):
        linha = []
        print(f"═══ Tanque {i + 1}: ═══")
        for j in range(colunas):
            while True:
                try:
                    valor = float(input(f"  Sensor {j + 1}: "))
                    linha.append(valor)
                    break # Sai do while True e vai para o próximo sensor
                except ValueError:
                    print("Valor inválido. Por favor, digite um número.")
        matriz.append(linha)

    return matriz

while opcaomenu != "4":
    print("╔══════════════════════════════════════╗")
    print("║     SISTEMA DE CONTROLE DE TANQUES   ║")
    print("║                                      ║")
    print("║  1. Coletar pH dos Tanques           ║")
    print("║  2. Validar Lotes                    ║")
    print("║  3. Acionar Válvulas de Escoamento   ║")
    print("║  4. Sair                             ║")
    print("╚══════════════════════════════════════╝")
    opcaomenu = input("Digite a opção desejada: ")

    if opcaomenu == "1":
        print("═══ COLETA DE pH DOS TANQUES ═══\n")
        print("Informe as leituras dos 3 sensores de pH para cada tanque\n")

        matriz_tanques = coletar_ph_tanques(4, 3)

        print("\nMatriz salva com sucesso!")
        print(matriz_tanques, "\n")
       


    elif opcaomenu == "2":
        print("teste 222222\n")
    elif opcaomenu == "3": 
        print("teste 333333\n")
    elif opcaomenu == "4":
        print("Saindo do sistema...\n")
    else: 
        print("Opção inválida.\n")
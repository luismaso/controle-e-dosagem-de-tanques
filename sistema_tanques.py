def coletar_ph_tanques(linhas, colunas):
    matriz = []

    for i in range(linhas):
        linha = []
        print(f"═══ Tanque {i + 1}: ═══")
        for j in range(colunas):
            while True:
                try:
                    valor = float(input(f"  Sensor {j + 1}: "))
                    if  0 <= valor <= 14:
                        linha.append(valor)
                        break
                    else:
                        print("Valor inválido. O pH deve estar entre 0 e 14.")
                except ValueError:
                    print("Valor inválido. Por favor, digite um número.")
        matriz.append(linha)
    return matriz   

def validar_lotes(matriz): 
    vetor_status = []
    for i in range(len(matriz)):
        soma = sum(matriz[i])
        quantidade = len(matriz[i])
        media = soma / quantidade

        if 6.5 <= media <= 7.5:
            status = 1
            print(f"Tanque {i+1}: Média = {media:.2f} - Status: Aprovado\n\n")
        else:
            status = 0 
            print(f"Tanque{i+1}: Média = {media:.2f} - Status: Reprovado\n\n")
        vetor_status.append(status)

    return vetor_status
    

opcaomenu = ""
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
        if len(matriz_tanques) == 0:
            print("Nenhuma matriz de tanques foi coletada.")
        else:
            vetor_status = validar_lotes(matriz_tanques)
                  
    elif opcaomenu == "3": 
        print("teste 333333\n")
    elif opcaomenu == "4":
        print("Saindo do sistema...\n")
    else: 
        print("Opção inválida.\n")
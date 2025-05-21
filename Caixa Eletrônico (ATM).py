import extratos

while True:
    #interface interativa
    print("================================================\n            CAIXA ELETRÔNICO           \n================================================")
    print("\n1. Ver Saldo\n2. Depositar\n3. Sacar\n4. Ver extrato de transações\n5. sair\n")
    opcao = int(input("..:"))
    #definir as funções
    def ver_saldo():
        with open("logger.txt", "r") as conteudo:
            conteudo = conteudo.read()
            print(f"Saldo atual: {conteudo}")
            return conteudo
        pass
    def depositar():
        with open("logger.txt", "r") as valor_antigo:
            valor_antigo = valor_antigo.read()
        if valor_antigo == '':
                with open("logger.txt", "w") as dep:
                    deposito_user = float(input("Qual valor será depositado: "))
                    dep.write(str(deposito_user))
                    print(f"Você depositou: {deposito_user}")
                    extratos.extrato.append(f"Você depositou: {deposito_user}")
        else:
            with open("logger.txt", "r") as valor_antigo1:
                valor_antigo1 = float(valor_antigo1.read())
            with open("logger.txt", "w") as dep:
                deposito_user = float(input("Qual valor será depositado: "))
                atualizar_valor = valor_antigo1 + deposito_user
                deposito = dep.write(str(atualizar_valor))
                print(f"Você depositou: {deposito_user}")
                extratos.extrato.append(f"Você depositou {deposito_user}")
    def sacar():
        with open("logger.txt", "r") as valor_antigo2:
            valor_antigo2 = valor_antigo2.read()
        if valor_antigo2 == '':
            print("Você não tem dinheiro pra sacar :(")
            extratos.extrato.append("Você tentou sacar mas não tinha saldo!")
        else:
            with open("logger.txt", "r") as valor_antigo3:
                valor_antigo3 = float(valor_antigo3.read())
                print(f"Você tem para sacar: {valor_antigo3}")
            with open("logger.txt", "w") as sac:
                sacar_user = float(input("Qual valor sacar: "))
                if sacar_user > valor_antigo3:
                    print("Você está tentando sacar uma quantia que não tem! :(")
                    extratos.extrato.append("Você tentou sacar uma quantia que não tinha!")
                    sac_error = sac.write(str(valor_antigo3))
                else:
                    atualizar_valor2 = valor_antigo3 - sacar_user
                    sacou = sac.write(str(atualizar_valor2))
                    print(f"Você sacou: {sacar_user}")
                    print(f"Seu saldo atual é: {atualizar_valor2}")
                    extratos.extrato.append(f"Você sacou: {sacar_user}")
    def extrato():
        print(extratos.extrato)
    def sair():
        exit()
    if opcao == 1:
        ver_saldo()
    if opcao == 2:
        depositar()
    if opcao == 3:
        sacar()
    if opcao == 4:
        extrato()
    if opcao == 5:
        sair()
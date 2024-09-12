menu = """
------------------MENU------------------
(S) Sacar
(D) Depositar
(V) Visualizar
(X) Sair
----------------------------------------
Digite a letra da operação desejada: 
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    operacao = input(menu)
    if operacao == "D":
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor digitado não é válido.")

    elif operacao == "S":
        valor = float(input("Informe o valor a ser sacado: "))

        excede_saldo = valor > saldo

        excede_limite = valor > limite

        excede_saques = numero_saques >= LIMITE_SAQUES

        if excede_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excede_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excede_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif operacao == "V":
        print("----------------EXTRATO----------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------------------------")
    elif operacao == "X":
        print("Obrigado por usar o nosso banco! Tenha um bom dia.")
        break
    else:
        print("Operação inválida! Digite novamente.")
def deposito(*, valor_antigo, valor_deposito):
    if valor_deposito < 0:
        print(f"O valor inserido para depósito é inválido.\n")
        return valor_antigo, None
    else:
        valor_atual = valor_antigo + valor_deposito
        print(f"Valor anterior: {valor_antigo}")
        print(f"Valor após depósito: {valor_atual}\n")
        nova_operacao = add_operacao_extrato("deposito", valor_antigo = valor_antigo, valor_atual = valor_atual, valor_auxiliar = valor_deposito)
        return valor_atual, nova_operacao

def saque(*, valor_saque, valor_antigo):
    if valor_saque > valor_antigo:
        print(f"Valor de saque maior do que o valor atual!\n")
        return valor_antigo, None
    elif valor_saque < 0:
        print(f"O valor inzerido para saque é inválido.\n")
        return valor_antigo, None
    else:
        valor_atual = valor_antigo - valor_saque
        print(f"Valor anterior: {valor_antigo}")
        print(f"Valor após saque: {valor_atual}\n")
        nova_operacao = add_operacao_extrato("saque", valor_antigo = valor_antigo, valor_atual = valor_atual, valor_auxiliar = valor_saque)
        return valor_atual, nova_operacao
    
def add_operacao_extrato(operacao, *, valor_antigo, valor_atual, valor_auxiliar):
    if(operacao == "deposito"):
        nova_operacao = f"Depósito\n{valor_antigo} + {valor_auxiliar} = {valor_atual}\n"
    elif(operacao == "saque"):
        nova_operacao = f"Saque\n{valor_antigo} - {valor_auxiliar} = {valor_atual}\n"
    return nova_operacao

def extrato(extrato_lista):
    if len(extrato_lista) > 0:
        print()
        for operacao in extrato_lista:
            print(operacao)
    else:
        print("\nNão há operações feitas nessa conta.\n")

def menu(saldo):
    opcao = "a"
    lista_extrato = []

    while opcao.lower() != "q":
        print("MENU".center(40,"-"))
        opcao = input(f"""
[E] - Extrato
[D] - Depósito
[S] - Saque
[Q] - Sair
                      
""").strip().lower()
        if opcao == "d": 
            print("DEPÓSITO".center(40,"-"))
            valor_deposito = float(input("\nValor que será depositado: "))
            saldo, nova_operacao = deposito(valor_antigo = saldo, valor_deposito = valor_deposito)
            if nova_operacao:
                lista_extrato.append(nova_operacao)
        elif opcao == "s":
            print("SAQUE".center(40,"-"))
            valor_saque = float(input("\nValor que será sacado: "))
            saldo, nova_operacao = saque(valor_saque = valor_saque, valor_antigo = saldo)
            if nova_operacao:
                lista_extrato.append(nova_operacao)
        elif opcao == "e":
            print("EXTRATO".center(40,"-"))
            extrato(lista_extrato)
        elif opcao == "q":
            print("Saindo...")
        else:
            print("Opção inválida.")

def banco():
    print("SISTEMA BANCÁRIO".center(40,"="))
    print()
    saldo = float(input("Saldo em conta: "))
    print()
    menu(saldo)

banco()
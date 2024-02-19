def depositar(valor_total, recebe_deposito):
    valor = float(input("Insira o valor de depósito: "))
    if valor <= 0:
        print("Valor inválido")
    else:
        valor_total += valor
        recebe_deposito += valor
        print("Depósito finalizado com sucesso!")
    return valor_total, recebe_deposito

def sacar(valor_total, quantidade_de_saque_diario, recebe_saque):
    if quantidade_de_saque_diario > 3:
        print("Limite de saques diários já atingido")
    else:
        valor = float(input("Insira o valor do saque: "))
        if valor > 0 and valor <= 500:
            if valor > valor_total:
                print(f"Saldo insuficiente, você tem R$ {valor_total:.2f} e sua tentativa de saque é superior ao valor desejado")
            else:
                valor_total -= valor
                quantidade_de_saque_diario += 1
                recebe_saque += valor
                print("Saque finalizado com sucesso!")
        else:
            print("O valor máximo que pode ser sacado é R$ 500.00")
    return valor_total, quantidade_de_saque_diario, recebe_saque

def mostrar_extrato(valor_total, recebe_deposito, recebe_saque, quantidade_de_saque_diario):
    print("==================SEU EXTRATO==================")
    print(f"Valor Depositado: R$ {recebe_deposito:.2f}")
    print(f"Valor na conta:   R$ {valor_total:.2f}")
    print(f"Valor Sacado:     R$ {recebe_saque:.2f}")
    print(f"Quantidade de vezes que o valor foi sacado: {quantidade_de_saque_diario}")
    print("================================================")
    
def main():
    valor_total = 0
    quantidade_de_saque_diario = 0
    recebe_deposito = 0
    recebe_saque = 0

    while True:
        menu = """
=================SEJA BEM VINDO=================

    1 - Depositar
    2 - Sacar 
    3 - Mostrar Extrato 
    0 - Sair  

================================================
"""
        print(menu)
        opcao = int(input("->"))

        if opcao == 1:
            valor_total, recebe_deposito = depositar(valor_total, recebe_deposito)
        elif opcao == 2:
            valor_total, quantidade_de_saque_diario, recebe_saque = sacar(valor_total, quantidade_de_saque_diario, recebe_saque)
        elif opcao == 3:
            mostrar_extrato(valor_total, recebe_deposito, recebe_saque, quantidade_de_saque_diario)
        elif opcao == 0:
            print("Você saiu do programa. Volte mais vezes!")
            break
        else:
            print("Opção inválida")

    print("Encerrando programa.....")

if __name__ == "__main__":
    main()

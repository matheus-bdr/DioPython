valor_total = 0
quantidadeDeSaqueDiario = 0
recebeSaque = 0 
recebeDeposito = 0

menu = f"""
=================SEJA BEM VINDO=================

    1 - Depositar
    2 - Sacar 
    3 - Mostrar Extrato 
    0 - Sair  

================================================
"""
print(menu)
opcao = int(input("->"))
while(opcao==1 or opcao==2 or opcao==3 or opcao==0):
    if opcao==1:
        valor = 0
        valor = float(input("Insira o valor de deposito: "))
        if valor<=0:
            print("Valor invalido ")
        else:
            deposito = valor
            valor_total = valor_total + deposito 
            recebeDeposito = deposito + recebeDeposito
            print("Deposito finalizado com sucesso!")

            print(menu)
            opcao = int(input("->"))

    elif opcao==2:
        if quantidadeDeSaqueDiario>3:
            print("Limite de Saques diários já feita ")
            print(menu)
            opcao = int(input("->"))
        else:
            quantidadeDeSaqueDiario = quantidadeDeSaqueDiario + 1
            if quantidadeDeSaqueDiario<=3:
                valor = 0
                valor = float(input("Insira o valor do saque: "))
                if valor <500 and valor>0:
                    saque = valor 
                    if saque > valor_total:
                        print(f"Saldo insuficiente, voce tem {valor_total} e sua tentativa de saque é superior o valor desejado")
                        print(menu)
                        opcao = int(input("->"))
                    else:
                        valor_total = valor_total - saque
                        recebeSaque = saque + recebeSaque
                        print("Saque finalizado com sucesso!")
                        
                        print(menu)
                        opcao = int(input("->"))
                else:
                    print("O valor maximo que pode ser sacado é R$ 500.00")
                    print(menu)
                    opcao = int(input("->"))
            else:
                print(f"Voce já realizou {quantidadeDeSaqueDiario-1} saques, tente novamente amanhã")
                print(menu)
                opcao = int(input("->"))
        

    elif opcao==3:
        print(
f"""
==================SEU EXTRATO==================

    Valor Depositado: R$ {recebeDeposito:.2f} 
    Valor na conta:   R$ {valor_total:.2f}
    Valor Sacado:     R$ {recebeSaque:.2f}
    Quantidade de 
    vezes que o 
    valor foi sacado: {quantidadeDeSaqueDiario-1} 
        

================================================
""")
        
        print(menu)
        opcao = int(input("->"))

    elif opcao==0:
        print("Voce saiu do programa, volte mais vezes!")
        break
    else:
        print("Opcao invalida")

print("Encerrando programa.....")
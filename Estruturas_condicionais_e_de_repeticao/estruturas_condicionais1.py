saldo = 2000
saque = float(input("informe o valor do seu saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")
saldo = 1000
saque = 100

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
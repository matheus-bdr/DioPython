def exibir_mensagem():
    print("Ola mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}")
# valor defaut valor
def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}")


exibir_mensagem()
exibir_mensagem2(nome="Bedas")
exibir_mensagem3()

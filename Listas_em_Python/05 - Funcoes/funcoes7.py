def somar(a,b):
    return a+b
def subtrair(a,b):
    return a-b
def exibir_resutado(a,b,funcao):
    resultado = funcao(a,b) #acessando a funcao somar
    print(f"O resultado da operacao é de = {resultado}")

exibir_resutado(10,10,somar)
exibir_resutado(10,10,subtrair)
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

soma = calcular_total([10,20,30,40]) 
antecessor_e_sucessor = retorna_antecessor_e_sucessor(20) 
print(soma)
print(antecessor_e_sucessor)
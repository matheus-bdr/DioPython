salario = 2000

def salario_bonus(bonus):
    global salario 
    # é necessário que voce chame ela como variavel global 
    salario+=bonus
    return salario

salario_bonus(500)
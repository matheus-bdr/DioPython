conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

#todos os elementos de um conjunto estão no outro:
a_tem_todos_elementos = conjunto_a.issuperset(conjunto_b)
print(a_tem_todos_elementos)
b_tem_todos_elementos = conjunto_b.issuperset(conjunto_a)
print(b_tem_todos_elementos)
lista = [1,"Bedas",[10,11,12]]

copia_da_lista = lista.copy()

print(copia_da_lista)


#print(id(copia_da_lista), id(lista))


copia_da_lista[2] = "Matheus" #trocando o valor da lista

print(copia_da_lista) 
print(lista) 
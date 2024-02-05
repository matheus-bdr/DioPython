curso = "pYtHoN"

print(curso.upper()) #deixa tudo em capslook
print(curso.lower()) #deixa tudo em minusculo
print(curso.title()) #deixa apenas a primeira em maiusculo 


curso2 = "   Python "

print(curso2.strip()) #tira os espaços do começo e final
print(curso2.lstrip()) #tira os espaços do começo L = left
print(curso2.rstrip()) # tira os espaços do final R = right

curso3 = "Python"

print(curso3.center(10, "#")) #coloca elementos entre sua string até dar a quantidade de elementos que é passada no primeiro parametro
print(".".join(curso3)) #insere o texto escolhido no meio da string
print(curso3.r()) # tira os espaços do final R = right
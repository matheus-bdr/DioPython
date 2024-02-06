linguagens = ["python","js","c", "csharp"]
print(linguagens.sort())   #ordena alfabéticamente
print(linguagens.sort(reverse=True)) #coloca a lista ao contrario
print(linguagens.sort(key=lambda x: len(x))) #ordenando por tamanho da string(crescente)
print(linguagens.sort(key=lambda x: len(x), reverse=True)) #ordenando por tamanho da string(decrescente) 

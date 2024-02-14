#valores unicos, não ordenadas e chave e valor
#valores tem que ser imutáveis 
pessoa = {"nome":"bedas", 
          "idade":"21"}

carro = dict(nome="bedas", idade=21)

#add valores
pessoa["telefone"] = "1111-1111"

#acessando valores 
pessoa["nome"]
pessoa["idade"]
pessoa["telefone"]

#alterando valores
pessoa["nome"] = "Matheus"
pessoa["idade"] = 22
pessoa["telefone"] = "2222-2222"

#criando chaves sem valores 
pessoa = dict.fromkeys(["nome","data"],"vazio")
#criando chaves com valores vazios
pessoa = dict.fromkeys(["nome","data"],"vazio")
#Acessando valores
pessoa.get("chave")
pessoa.get("chave",{})

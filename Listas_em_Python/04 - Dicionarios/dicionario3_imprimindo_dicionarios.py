#chave tem que ser imutavel
contatos = {
    "bedas@gmail.com": {"nome": "bedas", "telefone":1111111},
    "matheus@gmail.com": {"nome": "matheus", "telefone":1222111},
    "flamengo@gmail.com": {"nome": "flamenho", "telefone":1112111}
}

numero_do_bedas = contatos["bedas@gmail.com"]["telefone"]
print(numero_do_bedas)

print("___________________________")
for chave in contatos:
    print(chave, contatos[chave])
print("___________________________")
#retorna o mesmo resultado mas em tuplas
for chave, valor in contatos.items():
    print(chave, valor)
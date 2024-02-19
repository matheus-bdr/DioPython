def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# INSERINDO COM PARAMETROS NORMAIS (desvantajoso por conta de confusão do usuário)
salvar_carro("Fiat", "Uno Milles", 1984, "BDR-3333")
# INSERINDO DADOS DIRETAMENTE NOS PARAMETROS GUIADOS 
salvar_carro(marca="Fiat" , modelo = "Uno Milles" , ano =  1984, placa= "BDR-3333")
# INSERINDO DADOS COM UM DICIONÁRIO (kargs = KEYS ARGUMENTS)
salvar_carro(**{"marca":"Fiat" , "modelo":"Uno Milles" , "ano":1984, "placa":"BDR-3333"})
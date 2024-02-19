def criar_carro(modelo , ano , placa , / , marca , motor , combustivel ):
    # voce pode passar os parametros após a barra nomeados ou só com posicao
    # voce nao pode passar os parametros antes da barra com keywords
    print(f"{modelo}, {ano}, {placa}, {marca}, {motor}, {combustivel}")


criar_carro("Uno Milles",1984,"bdr-3333",marca="Fiat",motor="1.0", combustivel="flex: aqui sabe muito")
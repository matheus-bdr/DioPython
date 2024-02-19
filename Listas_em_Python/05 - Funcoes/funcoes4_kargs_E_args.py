def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in 
                            kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sexta-Feira", 
             "23 de agosto de 1999",
             "Zen of Python",
            "1 - Beautiful is better than ugly.", #neste momento, os valores estão mapeados com chave e valor  
            "2 - Beautiful is better than ugly.", #neste momento, os valores estão mapeados com chave e valor  
            "3 - Beautiful is better than ugly.", #neste momento, os valores estão mapeados com chave e valor  
            "4 - Beautiful is better than ugly.", #neste momento, os valores estão mapeados com chave e valor  
            "5 - Beautiful is better than ugly.", #neste momento, os valores estão mapeados com chave e valor  
            "6 - Beautiful is better than ugly.", #neste momento, os valores estão mapeados com chave e valor  
             autor="tim Peters", ano=1999)
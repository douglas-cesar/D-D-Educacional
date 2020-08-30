import principal

cnpj = int(input('cnpj '))
nome_escola = input('nome_escola')
cidade = input('cidade')
telefone = input('telefone')
endereco = input('endereco')


principal.insert_escola(cnpj, nome_escola,cidade, telefone,  endereco)

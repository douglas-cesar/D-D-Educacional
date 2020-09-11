import sqlite3
import factory_aluno

conn = sqlite3.connect('EDUCACIONAL.db')
cursor = conn.cursor()

def menu_aluno():
    print('''    +----------------------------------------------+
    |[ 1 ] Cadastrar aluno no sistema              |
    |[ 2 ] Visualizar dados do aluno               |
    |[ 3 ] Deletar aluno                           |
    |[ 4 ] Alterar dados cadastrais                |
    |[ 5 ] Verificar notas e frequência            |
    |[ 6 ] Voltar para o Menu principal            |
    +----------------------------------------------+''')
    op = int (input("> Informe a opção: "))
    if op == 1:
        create_aluno()

    elif op == 2:
        read_aluno()

    elif op == 3:
        delete_aluno()

    elif op == 4:
        update_aluno()
	
    elif op == 6:
	    menu_princ()
	
    elif op == 'S':
		print ("Até logo!")
		exit()
	
    else:
	    print ("Opção inválida. Tente Novamente")


menu_aluno()

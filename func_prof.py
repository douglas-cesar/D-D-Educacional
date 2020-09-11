import sqlite3
conn = sqlite3.connect('EDUCACIONAL.db')
cursor = conn.cursor()

def menu_prof():
    print('''    +----------------------------------------------+
    |[ 1 ] Cadastrar professor no sistema          |
    |[ 2 ] Visualizar professores cadastrados      |
    |[ 3 ] Deletar professor                       |
    |[ 4 ] Alterar dados dos professores           |
    |[ 6 ] Voltar para o Menu principal            |
    +----------------------------------------------+''')
    op = int (input("> Informe a opção: "))
    
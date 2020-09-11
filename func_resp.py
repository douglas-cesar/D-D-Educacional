import sqlite3
conn = sqlite3.connect('EDUCACIONAL.db')
cursor = conn.cursor()

def menu_resp():
    print('''    +----------------------------------------------+
    |[ 1 ] Cadastrar responsáveis                  |
    |[ 2 ] Selecionar responsáveis                 |
    |[ 3 ] Deletar responsável                     |
    |[ 4 ] Alterar dados do resposnável            |
    |[ 6 ] Voltar para o Menu principal            |
    +----------------------------------------------+''')
    op = int (input(">Informe a opção: "))
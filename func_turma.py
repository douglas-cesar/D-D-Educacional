import sqlite3
conn = sqlite3.connect('EDUCACIONAL.db')
cursor = conn.cursor()

def menu_turma():
    print('''    +----------------------------------------------+
    |[ 1 ] Cadastrar turma                         |
    |[ 2 ] Vizualizar turmas cadastrados           |
    |[ 3 ] Deletar turma                           |
    |[ 4 ] Alterar dados das turmas                |
    |[ 6 ] Voltar para o Menu principal            |
    +----------------------------------------------+''')
    op = int (input(">Informe a opção: "))
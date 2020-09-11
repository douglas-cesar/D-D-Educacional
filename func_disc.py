import sqlite3
conn = sqlite3.connect('EDUCACIONAL.db')
cursor = conn.cursor()

def menu_disc():
    print('''    +----------------------------------------------+
    |[ 1 ] Cadastrar nova disciplina               |
    |[ 2 ] Selecionar disciplinas cadastradas      |
    |[ 3 ] Deletar disciplina                      |
    |[ 4 ] Alterar dados das disciplinas           |
    |[ 6 ] Voltar para o Menu principal            |
    +----------------------------------------------+''')
    op = int (input(">Informe a opção: "))
import sqlite3
conn = sqlite3.connect('EDUCACIONAL.db')
cursor = conn.cursor()

def create_aluno():
    nome = (input('Nome completo: '))
    dt_nascimento = (input('Data de nascimento: '))
    idade = (input('Idade: '))
    cd_turma = (input('Código da turma: '))
    cpf = (input('CPF: '))
    id_resp = (input('Responsáveis: '))
    

    cursor.execute('''INSERT INTO ALUNO (nome, dt_nascimento, idade, cd_turma, cpf, id_resp) 
        VALUES (?, ?, ?, ?, ?, ?)''',(nome, dt_nascimento, idade, cd_turma, cpf, id_resp))
    print ("Aluno cadastrado com sucesso!")
    
    conn.commit()


def read_aluno():
    id = (input("Informe o ID do aluno: "))
    cursor.execute ("""SELECT * FROM ALUNO 
        WHERE id = ?""", (id))
    for linha in cursor.fetchall():
        print(linha)


def delete_aluno():
    	id = (input("Informe o ID do aluno: "))
        cursor.execute("""DELETE FROM ALUNO
        WHERE id = ?""" (id))

        conn.commit()


def update_aluno():
    id = (input("Informe o ID do aluno: "))
    novo_nome = input ("Digite o novo nome: ")
    nova_dt_nasc = input ("Digite a data de nascimento: ")
    nova_idade = input ("Digite a idade: ")
    novo_cd_turma = input ("Digite o código da turma: ")
    novo_cpf = input ("Digite o CPF: ")
    novo_resp = input ("Digite o ID do responsável: ")

    cursor.execute ("""UPDATE ALUNO
    
    SET nome = ?, dt_nascimento = ?, idade = ?, cd_turma = ?, cpf = ?, id_resp = ?
    WHERE id = ?""", (nome, dt_nascimento, idade, cd_turma, cpf, id_resp, id))

    conn.commit()
	
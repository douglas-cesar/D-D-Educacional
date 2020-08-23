import sqlite3

conn = sqlite3.connect('Academico.db')
cur = conn.cursor()


def create_sql():  # Funcao CRIAR
    cur.execute('''CREATE TABLE ESCOLA (
    cnpj INTEGER PRIMARY KEY UNIQUE,
    nome_escola CHARACTER NOT NULL,
    cidade CHARACTER NOT NULL,
    telefone VARCHAR NOT NULL,
    endereco VARCHAR NOT NULL
    );''')

    cur.execute('''CREATE TABLE TURMA (
    codigo INTEGER PRIMARY KEY,
    id_disciplina INTEGER NOT NULL,
    nome VARCHAR NOT NULL,
    turno CHARACTER NOT NULL,
    FOREIGN KEY (id_disciplina)
    REFERENCES DISCIPLINA (id)
    );''')

    cur.execute('''CREATE TABLE PROFESSOR (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_disciplina INTEGER NOT NULL,
    nome VARCHAR NOT NULL,
    telefone VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    FOREIGN KEY (id_disciplina)
    REFERENCES DISCIPLINA (id)
     );''')

    cur.execute('''CREATE TABLE DISCIPLINA (
    id_professor INTEGER NOT NULL,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR NOT NULL,
    FOREIGN KEY (id_professor)
    REFERENCES PROFESSOR (id)
    );''')

    cur.execute('''CREATE TABLE ALUNO (
    cpf INTEGER PRIMARY KEY,
    nome VARCHAR NOT NULL,
    dt_nascimento DATE NOT NULL,
    idade INTEGER NOT NULL,
    cd_turma VARCHAR NOT NULL,
    id_resp INTEGER NOT NULL,
    FOREIGN KEY (cd_turma) REFERENCES TURMA (codigo),
    FOREIGN KEY (id_resp) REFERENCES RESPONSAVEL (id)
    );''')

    cur.execute('''CREATE TABLE RESPONSAVEL (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf INTEGER NOT NULL,
    rg INTEGER NOT NULL,
    nome VARCHAR NOT NULL,
    dt_nascimento DATE NOT NULL,
    FOREIGN KEY (cpf)
    REFERENCES ALUNO(CPF)
    );''')
    conn.commit()

def insert_escola(cnpj, nome_escola,cidade, telefone,  endereco ):
    cur.execute(f''' INSERT INTO escola (cnpj, nome_escola, cidade, telefone, endereco) 
                     VALUES ({cnpj}, '{nome_escola}', '{cidade}', '{telefone}','{endereco}');''')
    conn.commit()






#create_sql()






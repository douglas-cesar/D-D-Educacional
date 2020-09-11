import sqlite3

conn = sqlite3.connect('EDUCACIONAL.db')
cur = conn.cursor()


def create_sql(conn, cur):
    cur.execute('''CREATE TABLE ESCOLA (
    cnpj INTEGER (14) PRIMARY KEY UNIQUE,
    nome_escola CHARACTER (50) NOT NULL,
    cidade CHARACTER (50) NOT NULL,
    telefone VARCHAR (10) NOT NULL,
    endereco VARCHAR (50) NOT NULL);''')

    cur.execute('''CREATE TABLE TURMA (
    nome VARCHAR (6) PRIMARY KEY,
    turno CHARACTER (6) NOT NULL,
    id_disciplina INTEGER (2) NOT NULL,
    FOREIGN KEY (id_disciplina)
    REFERENCES DISCIPLINA (id));''')

    cur.execute('''CREATE TABLE PROFESSOR (
    id INTEGER PRIMARY KEY,
    nome VARCHAR (50) NOT NULL,
    id_disciplina INTEGER (2) NOT NULL,
    telefone VARCHAR (10) NOT NULL,
    email VARCHAR (50) NOT NULL,
    FOREIGN KEY (id_disciplina)
    REFERENCES DISCIPLINA (id));''')

    cur.execute('''CREATE TABLE DISCIPLINA (
    id INTEGER (2) PRIMARY KEY,
    nome VARCHAR (50) NOT NULL,
    id_professor INTEGER (2) NOT NULL,
    FOREIGN KEY (id_professor)
    REFERENCES PROFESSOR (id));''')

    cur.execute('''CREATE TABLE ALUNO (
    cpf INTEGER (11) PRIMARY KEY,
    nome VARCHAR (50) NOT NULL,
    dt_nascimento DATE  NOT NULL,
    idade INTEGER (2) NOT NULL,
    cd_turma VARCHAR  NOT NULL,
    id_resp INTEGER NOT NULL,
    FOREIGN KEY (cd_turma) REFERENCES TURMA (codigo),
    FOREIGN KEY (id_resp) REFERENCES RESPONSAVEL (id));''')

    cur.execute('''CREATE TABLE RESPONSAVEL (
    id INTEGER (2) PRIMARY KEY,
    cpf INTEGER (11) NOT NULL,
    rg INTEGER (7) NOT NULL,
    nome VARCHAR (50) NOT NULL,
    dt_nascimento DATE NOT NULL);''')
    conn.commit()

    cur.execute('''CREATE TABLE RESPONSAVEL (
    id INTEGER (2) PRIMARY KEY,
    cpf INTEGER (11) NOT NULL,
    rg INTEGER (7) NOT NULL,
    nome VARCHAR (50) NOT NULL,
    dt_nascimento DATE NOT NULL);''')
    conn.commit()


def insert_sql(conn, cur): #FUNCAO INSERIR
    cur.execute('''INSERT INTO  ESCOLA (cnpj, nome_escola, cidade, telefone, endereco)
                    VALUES ('99.999.999/9999.99', 'Múltipla Escolha', 'Bragança', '3333-4444','Rua 10, 111, Vila Rica, Pe')''')


    cur.execute('''INSERT INTO ALUNO (cpf, nome, dt_nascimento, idade, cd_turma, id_resp) 
                   VALUES ('11122233344', 'Deyvid Lins','30/03/2006', 14, '9.1M', 1);''')

    cur.execute('''INSERT INTO ALUNO (cpf, nome, dt_nascimento, idade, cd_turma, id_resp) 
                    VALUES ('55566677788', 'Douglas César','25/01/2007', 13, '8.1T', 2);''')

    cur.execute('''INSERT INTO TURMA(nome, turno, id_disciplina)
                   VALUES('9.1M','MANHÃ', 1);''')

    cur.execute('''INSERT INTO TURMA(nome, turno, id_disciplina)
                   VALUES('8.1T','TARDE', 2);''')

    cur.execute('''INSERT INTO DISCIPLINA (id, nome, id_professor)
                   VALUES(1, 'PORTUGUÊS', 1);''')

    cur.execute('''INSERT INTO DISCIPLINA (id, nome, id_professor)
                   VALUES(2, 'MATEMÁTICA', 2);''')

    cur.execute('''INSERT INTO PROFESSOR (nome, id_disciplina, email, telefone)    
                   VALUES ('Helena Braga', 1, 'helena.braga@escola.com', '7777-8888');''')

    cur.execute('''INSERT INTO PROFESSOR (nome, id_disciplina, email, telefone)    
                   VALUES ('Rafael Melo', 2, 'rafael.melo@escola.com', '5555-6666');''')

    cur.execute('''INSERT INTO RESPONSAVEL (id, cpf, rg, nome, dt_nascimento)    
                   VALUES (1, '999.999.999.99', '9.999.999', 'Jaqueline César', '13/02/1976');''')

    cur.execute('''INSERT INTO RESPONSAVEL (id, cpf, rg, nome, dt_nascimento)    
                   VALUES (2, '888.888.888.88', '8.888.888', 'Taciana Lins', '31/06/1974');''')
 
    conn.commit()

conn.close()
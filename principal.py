import sqlite3
from reportlab.pdfgen import canvas

conn = sqlite3.connect('AcademicoD&D.db')
cur = conn.cursor()


def create_sql():  # Funcao CRIAR
    cur.execute('''CREATE TABLE ESCOLA (
    cnpj INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_escola CHARACTER NOT NULL,
    cidade CHARACTER NOT NULL,
    telefone VARCHAR NOT NULL,
    endereco VARCHAR NOT NULL
    );''')

    cur.execute('''CREATE TABLE TURMA (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    id_disciplina INTEGER NOT NULL,
    nome VARCHAR NOT NULL,
    turno CHARACTER NOT NULL,
    FOREIGN KEY (id_disciplina) REFERENCES DISCIPLINA (id)
    );''')

    cur.execute('''CREATE TABLE PROFESSOR (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_disciplina INTEGER NOT NULL,
    nome VARCHAR NOT NULL,
    salario DECIMAL NOT NULL,
    telefone VARCHAR NOT NULL,
    email VARCHAR NOT NULL,    
    FOREIGN KEY (id_disciplina) REFERENCES DISCIPLINA (id)
     );''')

    cur.execute('''CREATE TABLE DISCIPLINA (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR NOT NULL
    );''')

    cur.execute('''CREATE TABLE ALUNO (
    cpf INTEGER PRIMARY KEY,
    nome VARCHAR NOT NULL,
    dt_nascimento DATE NOT NULL,
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
    FOREIGN KEY (cpf) REFERENCES ALUNO(CPF)
    );''')
    conn.commit()

    cur.execute('''CREATE TABLE SITUACAO_ALUNO (
        id_disciplina INTEGER NOT NULL,
        cpf_aluno INTEGER,
        nota DECIMAL,
        falta VARCHAR(1),
        FOREIGN KEY(id_disciplina) REFERENCES disciplina(id),
        FOREIGN KEY (cpf_aluno) REFERENCES aluno(cpf)
        );''')
    conn.commit()

create_sql()

def insert_escola():
    cur.execute(''' INSERT INTO escola (cnpj, nome_escola, cidade, telefone, endereco) 
                     VALUES (109645454, 'D&D-Educacional', 'Jaboatão', '9999-9999','Rua 10');''')
    conn.commit()

def insert_disciplina(nom_disc):
    cur.execute(f''' INSERT INTO disciplina (id_professor, nome) 
                             VALUES ('{nom_disc}');''')
    conn.commit()

def insert_professor(id_disc, nom_prof,sal, telefone,email):
    cur.execute(f''' INSERT INTO professor (id_disciplina, nome, salario, telefone,email) 
                                 VALUES ({id_disc} ,'{nom_prof}', {sal}, '{telefone}', '{email}');''')
    conn.commit()

def insert_turma(cod_turm, id_disc, nom_tur, tur):
    cur.execute(f''' INSERT INTO turma (codigo, id_disciplina, nome, turno) 
                         VALUES ({cod_turm}, {id_disc}, '{nom_tur}', '{tur}');''')
    conn.commit()

def insert_responsavel(cpf, rg, nom_resp, dt_nasc):
    cur.execute(f''' INSERT INTO responsavel (cpf, rg, nome, dt_nascimento) 
                                 VALUES ({cpf} ,{rg},'{nom_resp}', '{dt_nasc}');''')
    conn.commit()

def insert_aluno(cpf,nom_al, dt_nasc, cod_tur, id_respo):
    cur.execute(f''' INSERT INTO aluno (cpf, nome, dt_nascimento, cd_turma, id_resp) 
                                 VALUES ({cpf} ,'{nom_al}','{dt_nasc}', {cod_tur}', {id_respo});''')
    conn.commit()

def insert_situacao_aluno(id_disc,cpf,nota,falta):
    cur.execute(f''' INSERT INTO aluno (id_disciplina,cpf,nota,falta) 
                                     VALUES ({id_disc} ,{cpf},{nota}, '{falta}');''')
    conn.commit()



for tabela in cur.execute('select * from escola;\n'):
    print(tabela)

''''pdf = canvas.Canvas('Arquivo.pdf')
pdf.drawString(200, 300, f'{tabela}')
pdf.save()'''

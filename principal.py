import sqlite3
from reportlab.pdfgen import canvas
from PIL import Image
import os

conn = sqlite3.connect('teste.db')
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
    dt_nascimento DATE NOT NULL
    );''')
    conn.commit()

    cur.execute('''CREATE TABLE SITUACAO_ALUNO (
        id_disciplina INTEGER NOT NULL,
        cpf_aluno INTEGER NOT NULL,
        nota DECIMAL,
        falta VARCHAR(1),
        FOREIGN KEY(id_disciplina) REFERENCES disciplina(id),
        FOREIGN KEY (cpf_aluno) REFERENCES aluno(cpf)
        );''')
    conn.commit()


# create_sql()

def insert_escola():
    cur.execute(''' INSERT INTO escola (cnpj, nome_escola, cidade, telefone, endereco) 
                     VALUES (109645454, 'D&D-Educacional', 'Jaboatão', '9999-9999','Rua 10');''')
    conn.commit()


def insert_disciplina(nom_disc):
    cur.execute(f''' INSERT INTO disciplina (nome) 
                             VALUES ('{nom_disc}');''')
    conn.commit()


def insert_professor(id_disc, nom_prof, sal, telefone, email):
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


def insert_aluno(cpf, nom_al, dt_nasc, cod_tur, id_respo):
    cur.execute(f''' INSERT INTO aluno (cpf, nome, dt_nascimento, cd_turma, id_resp) 
                                 VALUES ({cpf} ,'{nom_al}','{dt_nasc}', {cod_tur}, {id_respo});''')
    conn.commit()


def insert_situacao_aluno(cpf_aluno, id_disc, cpf, nota, falta):
    cur.execute(f''' INSERT INTO situacao_aluno (cpf_aluno,id_disciplina,cpf,nota,falta) 
                                     VALUES ({cpf_aluno},{id_disc} ,{cpf},{nota}, '{falta}');''')
    conn.commit()

nome = input('nome:')
c = cur.execute('SELECT nome FROM aluno')
for tabela in c:

  tab = ''.join(tabela) # Retira a virgula e paretenses das tuplas
  if nome == tab: #Verifica se o dado que o usuario digitou está igual ao do banco de dados
      cur.execute(f'''select a.nome, s.nota, s.falta
                                        from aluno as a
                                        inner join situacao_aluno as s
                                        on a.cpf = s.cpf_aluno where a.nome = '{nome}';\n''')

      mostrar = cur.fetchone()
      if mostrar is not None:
          print(mostrar)

      image= r"C:\Users\Deyvid\Desktop\ProjetoPython\D-D-Educacional\Academico\dd.jpg"

      pdf = canvas.Canvas('boletim.pdf') #Criar uma arquivo pdf chamado boletim
      pdf.drawImage(image,8,610)
      pdf.setFont("Helvetica-Bold", 24)
      pdf.drawString(200, 600, 'BOLETIM ESCOLAR:')
      pdf.drawString(200, 300, f'{mostrar}') #Escreve no arquivo que foi salvo
      pdf.save() #Salva todas as alterações
      break

else:
      print('Esse nome não existi')
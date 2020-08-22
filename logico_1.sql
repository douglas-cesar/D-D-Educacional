/* Lógico_2: */

CREATE TABLE ESCOLA (
    cnpj INTEGER PRIMARY KEY UNIQUE,
    nome_escola CHARACTER,
    cidade CHARACTER,
    telefone VARCHAR,
    endereco VARCHAR
);

CREATE TABLE TURMA (
    codigo INTEGER PRIMARY KEY,
    nome VARCHAR,
    turno CHARACTER,
    id_disciplina INTEGER
);

CREATE TABLE PROFESSOR (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR,
    id_disciplina INTEGER,
    telefone VARCHAR,
    email VARCHAR
);

CREATE TABLE DISCIPLINA (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR,
    id_professor INTEGER
);

CREATE TABLE ALUNO (
    cpf INTEGER PRIMARY KEY,
    nome VARCHAR,
    dt_nascimento DATE,
    idade INTEGER,
    cd_turma VARCHAR,
    id_mae INTEGER,
    id_pai INTEGER,
    FOREIGN KEY (cd_turma) REFERENCES TURMA (codigo),
    FOREIGN KEY (id_mae) REFERENCES MAE (id),
    FOREIGN KEY (id_pai) REFERENCES PAI (id)
);

CREATE TABLE MAE (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf INTEGER,
    rg INTEGER,
    nome VARCHAR,
    dt_nascimento DATE
);

CREATE TABLE PAI (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf INTEGER,
    rg INTEGER,
    nome VARCHAR,
    dt_nascimento DATE
);
 
ALTER TABLE TURMA ADD CONSTRAINT FK_TURMA_2
    FOREIGN KEY (id_disciplina)
    REFERENCES DISCIPLINA (id);
 
ALTER TABLE PROFESSOR ADD CONSTRAINT FK_PROFESSOR_2
    FOREIGN KEY (id_disciplina)
    REFERENCES DISCIPLINA (id);
 
ALTER TABLE DISCIPLINA ADD CONSTRAINT FK_DISCIPLINA_2
    FOREIGN KEY (id_professor)
    REFERENCES PROFESSOR (id);
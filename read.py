import sqlite3
# import create

conn = sqlite3.connect('EDUCACIONAL.db')
cur = conn.cursor()


def read_aluno():
	cur.execute('SELECT * FROM aluno')
	row = cur.fetchone()
	for linha in row:
    		return linha

	# cur.execute('''SELECT * FROM ALUNO\n''')
	
	# for linha in cur.execute('''SELECT * FROM ALUNO\n'''):
		# return (linha)




def read_professor(conn, cur):
	cur.execute('''SELECT * FROM PROFESSOR''')
	
	for linha in cur.fetchall():
    		print(linha)

def read_turma(conn, cur):
	cur.execute('''SELECT * FROM TURMA''')
	
	for linha in cur.fetchall():
    		print(linha)

def read_disciplina(conn, cur):
	cur.execute('''SELECT * FROM DISCIPLINA''')
	
	for linha in cur.fetchall():
		print(linha)

def read_escola(conn, cur):
	cur.execute('''SELECT * FROM ESCOLA''')
	
	for linha in cur.fetchall():
    		print(linha)

def read_responsavel(conn, cur):
	cur.execute('''SELECT * FROM RESPONSAVEL''')
	
	for linha in cur.fetchall():
		print(linha)


def select():
  mostrar = cur.execute('select * from aluno')
  for linha in mostrar:
      print (linha)

select()

conn.commit() 

read_aluno()

# conn.close()




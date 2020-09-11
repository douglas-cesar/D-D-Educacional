import sqlite3
import time
from func_aluno import menu_aluno 
from func_prof import menu_prof
from func_disc import menu_disc
from func_resp import menu_resp
from func_turma import menu_turma

conn = sqlite3.connect('EDUCACIONAL.db')
cursor = conn.cursor()

op = 0

def menu_princ():
	print ('''        +--------------------+
	|[ 1 ]. Aluno        |
	|[ 2 ]. Professor    |
	|[ 3 ]. Disciplinas  |
	|[ 4 ]. Responsáveis |
	|[ 5 ]. Turma        |
	+--------------------+''')
	op = int (input(">Informe a opção: "))
	if op == 1:
		menu_aluno()
	elif op == 2:
		menu_prof()
	elif op == 3:
		menu_disc()
	elif op == 4:
		menu_resp()
	elif op == 5:
		menu_turma()
	elif op == 'S':
		print ("Até logo!")
		sleep(2)
		exit()
	else:
		print ("Opção inválida. Tente Novamente")

menu_princ()

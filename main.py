import sqlite3
from menu import menu_princ
from func_aluno import menu_aluno
from func_prof import menu_prof
from func_turma import menu_turma

conn = sqlite3.connect('EDUCACIONAL.db')
cursor = conn.cursor()

menu_princ()
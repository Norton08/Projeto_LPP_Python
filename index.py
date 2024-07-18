import sys
import subprocess
import sqlite3
import time
import os
try:
	from tabulate import tabulate
except ImportError:
	print("O pacote 'tabulate' não está instalado. Instalando agora...")
	subprocess.check_call([sys.executable, "-m", "pip", "install", 'tabulate'])
	from tabulate import tabulate

# Função para criar a tabela de pessoas
def create_table():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS pessoas (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			nome TEXT NOT NULL,
			idade INTEGER NOT NULL,
			email TEXT NOT NULL
		)
	''')
	conn.commit()
	print('Tabela criada com sucesso!') 
	time.sleep(1)
	conn.close()

# Função para inserir uma pessoa na tabela
def insert_pessoa(nome, idade, email):
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		INSERT INTO pessoas (nome, idade, email)
		VALUES (?, ?, ?)
	''', (nome, idade, email))
	conn.commit()
	print('Pessoa inserida com sucesso!')
	conn.close()

# Função para atualizar os dados de uma pessoa na tabela
def update_pessoa(id, nome, idade, email):
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		UPDATE pessoas
		SET nome = ?, idade = ?, email = ?
		WHERE id = ?
	''', (nome, idade, email, id))
	conn.commit()
	print('Pessoa atualizada com sucesso!')
	conn.close()

# Função para deletar uma pessoa da tabela
def delete_pessoa(id):
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		DELETE FROM pessoas
		WHERE id = ?
	''', (id,))
	conn.commit()
	print('Pessoa excluída com sucesso!')
	conn.close()

# Função para buscar todas as pessoas na tabela
def select_all_pessoas():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		SELECT * FROM pessoas
	''')
	rows = cursor.fetchall()
	print('Query de busca feita com sucesso!')
	conn.close()
	return rows

# Função para buscar uma pessoa pelo ID na tabela
def select_pessoa_by_id(id):
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		SELECT * FROM pessoas
		WHERE id = ?
	''', (id,))
	row = cursor.fetchone()
	conn.close()
	return row

def menu():
	print('------------------')
	print('Menu')
	print('1 - Inserir pessoa')
	print('2 - Atualizar pessoa')
	print('3 - Buscar todas as pessoas')
	print('4 - Buscar pessoa por ID')
	print('5 - Deletar pessoa')
	print('6 - Sair')
	print('------------------')

	opcao = obter_opcao()
	return opcao

def obter_opcao():
	while True:
		opcao = input("Digite a opção desejada: ")
		if opcao.isdigit():
			opcao = int(opcao)
			return opcao
		else:
			print("Entrada inválida. Por favor, digite apenas números.")

def verificar_opcao(opcao):
	nomes_colunas = ["ID", "Nome", "Idade", "Email"]
	if opcao == 1:
		nome = input('Digite o nome da pessoa para inserir: ')
		idade = int(input('Digite a idade da pessoa para inserir: '))
		email = input('Digite o email da pessoa para inserir: ')
		insert_pessoa(nome, idade, email)
	elif opcao == 2:
		id = int(input('Digite o ID da pessoa que deseja atualizar: '))
		nome = input('Digite o novo valor do nome da pessoa: ')
		idade = int(input('Digite o novo valor da idade da pessoa: '))
		email = input('Digite o novo valor do email da pessoa: ')
		update_pessoa(id, nome, idade, email)
	elif opcao == 3:
		rows = select_all_pessoas()
		print(tabulate(rows, headers=nomes_colunas, tablefmt='grid'))
	elif opcao == 4:
		id = int(input('Digite o ID da pessoa que deseja buscar: '))
		row = select_pessoa_by_id(id)
		while True:
			if row is None:
				print('Não possui pessoa cadastrada com o id informado!')
				id = int(input('Digite um ID válido da pessoa que deseja buscar: '))
				row = select_pessoa_by_id(id)
			else:
				print('Query de busca por id feita com sucesso!')
				break
		row = [row]
		print(tabulate(row, headers=nomes_colunas, tablefmt='grid'))
	elif opcao == 5:
		id = int(input('Digite o ID da pessoa que deseja deletar: '))
		delete_pessoa(id)
	elif opcao == 6:
		print('Saindo!')
		exit()
	elif opcao < 1 or opcao > 6:
		print('Opção inválida!')

def main():
	# Criar a tabela de pessoas
	create_table()
	while True:
		opcao = menu()
		verificar_opcao(opcao)
		input("Pressione Enter para continuar...")
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear') 

if __name__ == '__main__':
	main()
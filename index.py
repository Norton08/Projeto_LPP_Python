import sqlite3

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
	conn.close()

# Função para buscar todas as pessoas na tabela
def select_all_pessoas():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		SELECT * FROM pessoas
	''')
	rows = cursor.fetchall()
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

# Criar a tabela de pessoas
create_table()
import sqlite3
from contextlib import closing

DATABASE_URL = "sqlite:///./database.db"  # Caminho do banco de dados


def create_connection():
    """Cria uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DATABASE_URL.split(':///')[1])
    return conn


def create_tables():
    """Cria as tabelas no banco de dados."""
    with closing(create_connection()) as conn:
        cursor = conn.cursor()

        # Criação da tabela de usuários
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,                
            )
        ''')

        conn.commit()


def populate_db():
    """Popula o banco de dados com dados iniciais."""
    with closing(create_connection()) as conn:
        cursor = conn.cursor()

        # Inserção de dados iniciais
        users = [
            ("Alice", "alice@example.com"),
            ("Bob", "bob@example.com"),
        ]

        cursor.executemany('''
            INSERT INTO users (name, email) VALUES (?, ?)
        ''', users)

        conn.commit()
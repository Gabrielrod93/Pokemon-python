#banco_de_dados.py
import sqlite3

def criar_tabela():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        nome text,
        id integer,
        habilidade text,
        movimento text
    )
    """)
    conn.commit()
    conn.close()

def inserir_pokemon(nome, id, habilidade_escolhida, movimentos_escolhidos):
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()

    movimentos_string = ",".join(movimentos_escolhidos)

    cursor.execute("""
    INSERT INTO pokemon (nome, id, habilidade, movimento)
    VALUES (?,?,?,?)
    """, (nome, id, habilidade_escolhida, movimentos_string))

    conn.commit()
    conn.close()



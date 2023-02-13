#banco_de_dados.py

from prettytable import PrettyTable
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


def excluir_pokemon(id):
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()

    cursor.execute(f'DELETE FROM pokemon WHERE id={id}')
    conn.commit()
    print(f'Pokemon com id {id} foi excluído com sucesso.')
    conn.close()

def limpar_banco_de_dados():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pokemon")

    conn.commit()
    print("Banco de dados foi limpo com sucesso.")
    conn.close()


def mostrar_time():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pokemon")
    resultados = cursor.fetchall()

    tabela = PrettyTable(["Nome", "ID", "Habilidade", "Movimentos"])
    for resultado in resultados:
        tabela.add_row(resultado)

    print(tabela)
    conn.close()
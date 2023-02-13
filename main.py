#main.py

import sqlite3
from fazendo_pokemeon import escolhendo_pokemon, escolhendo_movimentos, escolhendo_habilidade, inserir_no_time
from banco_de_dados import criar_tabela, excluir_pokemon, limpar_banco_de_dados, mostrar_time

def time_cheio():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM pokemon")
    resultado = cursor.fetchone()
    return resultado[0] >= 6

while True:
    print("Selecione uma opção:")
    print("1. Criar novo pokemon")
    print("2. Excluir Pokémon")
    print("3. Excluir time")
    print("4. Mostrar Pokémons adicionados")
    print("5. Encerrar o programa")

    opção = int(input("Digite a opção desejada (1, 2, 3, 4 ou 5): "))

    if opção == 1:
        if time_cheio():
            print("Seu time está cheio. Por favor exclua um Pokémon antes de adicionar outro.")
        else:
            escolhendo_pokemon()
            escolhendo_habilidade()
            escolhendo_movimentos()
            inserir_no_time()

    elif opção == 2:
        mostrar_time()
        id = input('Qual Pokémon você gostaria de excluir?')
        excluir_pokemon(id)

    elif opção == 3:
        limpar_banco_de_dados()
        
    elif opção == 4:
        mostrar_time()

    elif opção == 5:
        print("O programa está sendo encerrado...")
        exit()

    else:
        print("Opção inválida, por favor selecione 1, 2, 3, 4 ou 5.")

criar_tabela()

#main.py
from banco_de_dados import inserir_pokemon
from requisicoes_api import buscar_pokemon, buscar_habilidades, buscar_movimentos

def escolhendo_pokemon():
    while True:
        nome_pokemon = input('Escolha seu Pokemon! ').lower().strip()
        poke = buscar_pokemon(nome_pokemon)
        if not poke:
            print(f"Desculpe, o Pokemon {nome_pokemon} não foi encontrado na API.")
        else:
            global nome
            nome = poke['name']
            global id
            id = poke['id']
            print(f'Você escolheu {nome}')
            break

def escolhendo_movimentos():
    movimentos = buscar_movimentos(id)
    if not movimentos:
        print("Desculpe, não foi possível buscar os movimentos do Pokemon escolhido.")
        return
    for i, movimento in enumerate(movimentos):
        print(f'{i + 1}. {movimento}')
    global movimentos_escolhidos
    movimentos_escolhidos = []
    num_movimentos = min(len(movimentos), 4)
    for i in range(num_movimentos):
        escolhida = int(input(f'Escolha o {i + 1}º movimento acima: ')) - 1
        while escolhida < 0 or escolhida >= len(movimentos):
            print("Desculpe, a opção escolhida não é válida.")
            escolhida = int(input(f'Escolha o {i + 1}º movimento acima: ')) - 1
        movimentos_escolhidos.append(movimentos[escolhida])



def escolhendo_habilidade():
    habilidades = buscar_habilidades(id)
    while True:
        for i, habilidade in enumerate(habilidades):
            print(f'{i + 1}. {habilidade}')
        escolhida = int(input('Escolha uma das habilidades acima: ')) - 1
        global habilidade_escolhida
        try:
            habilidade_escolhida = habilidades[escolhida]
            break
        except IndexError:
            print("Desculpe, a opção escolhida não é válida.")

def inserir_no_time():
    inserir_pokemon(nome, id, habilidade_escolhida, movimentos_escolhidos)
    print (f"{nome} com id {id}, habilidade {habilidade_escolhida} e os movimentos: {movimentos_escolhidos} foram adicionados ao seu time Pokemon!.")


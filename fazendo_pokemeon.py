#fazendo_pokemon.py
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
    for i, movimento in enumerate(movimentos):
        print(f'{i + 1}. {movimento}')
    global movimentos_escolhidos
    movimentos_escolhidos = []
    num_movimentos = min(len(movimentos), 4)
    for i in range(num_movimentos):
        while True:
            escolhida = input(f'Escolha o {i + 1}º movimento acima ou digite o nome do movimento: ')
            try:
                escolhida = int(escolhida) - 1
                if escolhida < 0 or escolhida >= len(movimentos):
                    print("Desculpe, a opção escolhida não é válida.")
                elif movimentos[escolhida] in movimentos_escolhidos:
                    print("Desculpe, você já escolheu esse movimento.")
                else:
                    movimentos_escolhidos.append(movimentos[escolhida])
                    break
            except ValueError:
                if escolhida in movimentos and escolhida not in movimentos_escolhidos:
                    movimentos_escolhidos.append(escolhida)
                    break
                else:
                    print("Desculpe, a opção escolhida não é válida.")


def escolhendo_habilidade():
    global habilidade_escolhida
    habilidades = buscar_habilidades(id)
    while True:
        for i, habilidade in enumerate(habilidades):
            print(f'{i + 1}. {habilidade}')
        escolhida = input('Escolha uma das habilidades acima ou digite o nome da habilidade: ')
        try:
            escolhida = int(escolhida) - 1
            habilidade_escolhida = habilidades[escolhida]
            break
        except (ValueError, IndexError):
            if escolhida in habilidades:
                habilidade_escolhida = escolhida
                break
            else:
                print("Desculpe, a opção escolhida não é válida.")
                
def inserir_no_time():
    inserir_pokemon(nome, id, habilidade_escolhida, movimentos_escolhidos)
    print (f"{nome} com id {id}, habilidade {habilidade_escolhida} e os movimentos: {movimentos_escolhidos} foram adicionados ao seu time Pokemon!.")


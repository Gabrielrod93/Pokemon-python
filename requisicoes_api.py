#requisicoes_api.py
import requests

def buscar_pokemon(nome):
    api = f'https://pokeapi.co/api/v2/pokemon/{nome}'
    res = requests.get(api)
    if res.status_code == 404:
        return None
    return res.json()

def buscar_habilidades(pokemon_id):
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    res = requests.get(api)
    poke = res.json()
    habilidades = [habilidade['ability']['name'] for habilidade in poke['abilities']]
    return habilidades

def buscar_movimentos(pokemon_id):
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    res = requests.get(api)
    poke = res.json()
    movimentos = {}
    movimentos = [movimento['move']['name'] for movimento in poke['moves']]
    return movimentos

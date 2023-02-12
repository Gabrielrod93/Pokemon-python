#main.py
from fazendo_pokemeon import escolhendo_pokemon, escolhendo_movimentos, escolhendo_habilidade, inserir_no_time
from banco_de_dados import criar_tabela, excluir_pokemon, limpar_banco_de_dados

print("Selecione uma opção:")
print("1. Criar novo time")
print("2. Excluir Pokémon")
print("3. Excluir time")

opção = int(input("Digite a opção desejada (1, 2 ou 3): "))

if opção == 1:
    escolhendo_pokemon()
    escolhendo_habilidade()
    escolhendo_movimentos()
    inserir_no_time()
elif opção == 2:
    id = input('Qual Pokemon você gostaria de excluir?')
    excluir_pokemon(id)

elif opção == 3:
    limpar_banco_de_dados()
else:
    print("Opção inválida, por favor selecione 1, 2 ou 3.")



if __name__ == '__main__':
    criar_tabela()
    for i in range(6):
        escolhendo_pokemon()
        escolhendo_habilidade()
        escolhendo_movimentos()
        inserir_no_time()
        

# Pokemon-python

Arquivo README para o projeto de Gerenciamento de Time de Pokémon
Este projeto permite que você crie, edite e exiba um time de Pokémons através de uma interface interativa. Ele usa o banco de dados SQLite para armazenar informações sobre cada Pokémon, incluindo o nome, o ID, a habilidade e os movimentos.

Requisitos
Python 3.x
Módulo SQLite3
Módulo prettytable
Instalação
Antes de usar o projeto, você precisa instalar as dependências usando o seguinte comando no terminal:

Copy code
pip install sqlite3 prettytable
Uso
Para iniciar o programa, execute o arquivo main.py no terminal com o comando:

css
Copy code
python main.py
Você será apresentado com uma interface interativa que permitirá:

Adicionar um novo Pokémon ao time
Excluir um Pokémon do time
Limpar o time inteiro
Mostrar os Pokémons adicionados ao time
Encerrar o programa
Estrutura de arquivos
Este projeto é composto pelos seguintes arquivos:

main.py: O arquivo principal que contém o código da interface interativa.
banco_de_dados.py: Este arquivo contém todas as funções relacionadas ao banco de dados, como criar tabelas, inserir, excluir e exibir informações do time.
fazendo_pokemon.py: Este arquivo contém todas as funções relacionadas a escolha de um Pokémon, incluindo a escolha de habilidades e movimentos.
Contribuições
Este é um projeto Open Source e todas as contribuições são bem-vindas. Se você encontrar algum bug ou desejar adicionar uma nova funcionalidade, sinta-se à vontade para abrir uma pull request.

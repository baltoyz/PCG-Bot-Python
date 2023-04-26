import requests
import random


def obterNome():
  # Faz uma requisição GET para a API da PokeAPI para obter a lista de todos os Pokémons
  response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1118")
  if response.status_code == 200:
    # Extrai a lista de resultados da resposta JSON
    results = response.json()["results"]
    # Seleciona um resultado aleatório da lista
    random_result = random.choice(results)
    # Extrai o nome do Pokémon selecionado
    pokemon_obtido = random_result["name"]
    # Imprime o nome do Pokémon selecionado
    print("O Pokémon aleatório selecionado é:", pokemon_obtido)
    return pokemon_obtido
  else:
    print("Não foi possível obter a lista de Pokémons da API.")
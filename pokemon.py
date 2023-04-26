import requests
from obterjwt import obterJWT


def obterPokemon():
  jwt = obterJWT()
  url = 'https://poketwitch.bframework.de/api/game/ext/trainer/pokemon/'
  headers = {
    'Accept':
    'application/json, text/plain, */*',
    'Authorization':
    jwt,
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
  }

  response = requests.get(url, headers=headers)
  data = response.json()
  allPokemon = data['allPokemon']
  for pokemon in allPokemon:
    name = pokemon['name']
    level = pokemon['lvl']
    baseStats = pokemon['baseStats']
    avgIV = int(pokemon['avgIV'])
    sellPrice = pokemon['sellPrice']
    nickname = pokemon['nickname']
    if nickname != 'trade':
      print(
        f'{name} | Level: {level} | Base Stats: {baseStats} | IV: {avgIV} | Preço: {sellPrice} |'
      )
  for pokemon in allPokemon:
    nickname = pokemon['nickname']
    identidade = pokemon['id']
    if nickname == 'trade':
      return identidade


obterPokemon()
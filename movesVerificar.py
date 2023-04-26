import requests
from obterjwt import obterJWT
from batalhaLista import pokemon_ids, pokemon_names

jwt = obterJWT
url_base = 'https://poketwitch.bframework.de/api/game/ext/trainer/pokemon/'

headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'pt-br',
  'Authorization': jwt,
  'Connection': 'keep-alive',
  'Host': 'poketwitch.bframework.de',
  'Origin': 'https://pm0qkv9g4h87t5y6lg329oam8j7ze9.ext-twitch.tv',
  'Referer': 'https://pm0qkv9g4h87t5y6lg329oam8j7ze9.ext-twitch.tv/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'cross-site',
  'Sec-GPC': '1',
  'User-Agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

for index, pokemon_id in enumerate(pokemon_ids):
  url = f'{url_base}{pokemon_id}/'
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    data = response.json()
    moves = [move['name'] for move in data['moves']]
    print(f'Moves do Pokemon ID {pokemon_names[index]}: {moves}')
  else:
    print(
      f"Erro na requisição para o Pokemon ID {pokemon_id}: {response.status_code}"
    )

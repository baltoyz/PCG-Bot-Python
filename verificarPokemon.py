import requests
from obterjwt import obterJWT
from pokemon import obterPokemon
import time

while True:
  jwt = obterJWT()
  identidade = obterPokemon()

  url = f'https://poketwitch.bframework.de/api/game/ext/trainer/pokemon/{identidade}/'

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

  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    data = response.json()
    tradable = data['tradable']
    print(f"POKEMON {tradable}")
  else:
    print(f"Erro na requisição: {response.status_code}")

  if tradable is None:
    url = f'https://poketwitch.bframework.de/api/game/ext/trainer/wonder-trade/{identidade}/'
    headers = {
      'Accept': 'application/json, text/plain, */*',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'en',
      'Authorization': jwt,
      'Connection': 'keep-alive',
      'Content-Length': '0',
      'Host': 'poketwitch.bframework.de',
      'Origin': 'https://pm0qkv9g4h87t5y6lg329oam8j7ze9.ext-twitch.tv',
      'Referer': 'https://pm0qkv9g4h87t5y6lg329oam8j7ze9.ext-twitch.tv/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'cross-site',
      'User-Agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
      'sec-ch-ua':
      '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"'
    }
    responseTrade = requests.post(url, headers=headers)
    if responseTrade.status_code == 200:
      print("Trade realizado com sucesso!")
    else:
      print(f"Erro na requisição de trade: {responseTrade.status_code}")

  time.sleep(300)

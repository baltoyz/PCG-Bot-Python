import requests
from obterjwt import obterJWT


def obterBolas():
  jwt = obterJWT()
  headers = {
    'Accept':
    'application/json, text/plain, */*',
    'Authorization':
    jwt,
    'Connection':
    'keep-alive',
    'Host':
    'poketwitch.bframework.de',
    'Origin':
    'https://pm0qkv9g4h87t5y6lg329oam8j7ze9.ext-twitch.tv',
    'Referer':
    'https://pm0qkv9g4h87t5y6lg329oam8j7ze9.ext-twitch.tv/',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
  }

  response = requests.get(
    'https://poketwitch.bframework.de/api/game/ext/trainer/inventory/',
    headers=headers)
  data = response.json()

  cash = data.get('cash')
  all_items = data.get('allItems', [])

  poke_ball = next((item for item in all_items if item['name'] == 'Poke Ball'),
                   None)
  great_ball = next(
    (item for item in all_items if item['name'] == 'Great Ball'), None)
  ultra_ball = next(
    (item for item in all_items if item['name'] == 'Ultra Ball'), None)
  dive_ball = next((item for item in all_items if item['name'] == 'Dive Ball'),
                   None)

  poke_ball_amount = poke_ball['amount'] if poke_ball else 0
  great_ball_amount = great_ball['amount'] if great_ball else 0
  ultra_ball_amount = ultra_ball['amount'] if ultra_ball else 0
  dive_ball_amount = dive_ball['amount'] if dive_ball else 0

  print(f"Total de Poke Balls: {poke_ball_amount}")
  print(f"Total de Great Balls: {great_ball_amount}")
  print(f"Total de Ultra Balls: {ultra_ball_amount}")
  print(f"Total de Dive Balls: {dive_ball_amount}")
  print(f"Cash: {cash}")
  item_names = [item['name'] for item in all_items]
  print(f"Itens no inventário: {', '.join(item_names)}")

  return {
    'dive_ball_amount': dive_ball_amount or 0,
    'cash': cash or 0,
    'poke_ball_amount': poke_ball_amount or 0,
    'great_ball_amount': great_ball_amount or 0,
    'ultra_ball_amount': ultra_ball_amount or 0,
  }

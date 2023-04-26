import requests
from obterjwt import obterJWT


def comprarBolas():
  jwt = obterJWT()
  url = "https://poketwitch.bframework.de/api/game/ext/shop/purchase/"
  headers = {
    'Authorization': jwt,
    "Content-Type": "application/json",
  }
  payload = {"item_name": "poke_ball", "amount": 1}
  response = requests.post(url, headers=headers, json=payload)
  print("Compra Realizada", response)

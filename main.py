import socket
import time
from arquivo import obterBolas
from testes import comprarBolas
from nomePokemon import obterNome
import random

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "your name here"
PASS = "xxxxxxxxxxxxxxx"
CHANNEL = "#live name here"


def connect():
  s = socket.socket()
  s.connect((HOST, PORT))
  s.send(f"PASS {PASS}\r\n".encode())
  s.send(f"NICK {NICK}\r\n".encode())
  s.send(f"JOIN {CHANNEL}\r\n".encode())
  return s


def main():
  s = connect()
  while True:
    try:
      resp = s.recv(2048).decode()
      if resp.startswith("PING"):
        s.send("PONG\n".encode())
      elif "PRIVMSG" in resp:
        username = resp.split("!")[0][1:]
        message = resp.split("PRIVMSG")[1].split(":")[1].rstrip()
        print(f"{username}: {message}")
        if username == "elbierro" and "Remember to get Poke-paid by being active in chat every 15 minutes" in message:
          pokemon_obtido = obterNome() or 'WhySoSerious'
          time.sleep(random.random() * 60)
          s.send(f"PRIVMSG {CHANNEL} :{pokemon_obtido}\r\n".encode())
        if username == "pokemoncommunitygame" and "!pokecatch" in message and "deemon8FishRed" not in message:
          result = obterBolas()
          pokemon_obtido = obterNome() or 'WhySoSerious'
          if result['poke_ball_amount'] > 0:
            time.sleep(random.random() * 60)
            s.send(f"PRIVMSG {CHANNEL} :!pokecatch\r\n".encode())
          elif result['cash'] > 300 and result['poke_ball_amount'] == 0:
            comprarBolas()
            time.sleep(random.random() * 60)
            s.send(f"PRIVMSG {CHANNEL} :!pokecatch\r\n".encode())
          else:
            time.sleep(random.random() * 60)
            s.send(f"PRIVMSG {CHANNEL} :{pokemon_obtido}\r\n".encode())

        elif username == "pokemoncommunitygame" and "!pokecatch" in message and "deemon8FishRed" in message:
          result = obterBolas()
          if result['dive_ball_amount'] > 0:
            time.sleep(random.random() * 60)
            s.send(f"PRIVMSG {CHANNEL} :!pokecatch diveball\r\n".encode())
          elif result['poke_ball_amount'] > 0:
            time.sleep(random.random() * 60)  # delay de 200ms
            s.send(f"PRIVMSG {CHANNEL} :!pokecatch\r\n".encode())
          elif result['cash'] > 300 and result['poke_ball_amount'] == 0:
            comprarBolas()
            time.sleep(random.random() * 60)
            s.send(f"PRIVMSG {CHANNEL} :!pokecatch\r\n".encode())
          else:
            time.sleep(random.random() * 60)
            s.send(f"PRIVMSG {CHANNEL} :{pokemon_obtido}\r\n".encode())

    except ConnectionResetError:
      print("Conexão interrompida, tentando reconectar...")
      time.sleep(10)
      s = connect()


if __name__ == "__main__":
  main()

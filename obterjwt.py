import requests


def obterJWT():
  url = "https://gql.twitch.tv/gql"

  headers = {
    "Authorization": "OAuth xxxxxxxxxxxxxxxxxxxxxxxxx",
    "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
    "Content-Type": "text/plain;charset=UTF-8",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Client-Version": "655b4ede-706b-4ab3-a6b4-7a6d86ccf8cb",
    "Origin": "https://www.twitch.tv",
    "Referer": "https://www.twitch.tv/",
  }

  payload = [
    {
      "operationName": "CoreActionsCurrentUser",
      "variables": {},
      "extensions": {
        "persistedQuery": {
          "version":
          1,
          "sha256Hash":
          "6b5b63a013cf66a995d61f71a508ab5c8e4473350c5d4136f846ba65e8101e95",
        }
      },
    },
    {
      "operationName": "ExtensionsForChannel",
      "variables": {
        "channelID": "246149775"
      },
      "extensions": {
        "persistedQuery": {
          "version":
          1,
          "sha256Hash":
          "d52085e5b03d1fc3534aa49de8f5128b2ee0f4e700f79bf3875dcb1c90947ac3",
        }
      },
    },
    {
      "operationName": "TrackingManager_RequestInfo",
      "variables": {},
      "extensions": {
        "persistedQuery": {
          "version":
          1,
          "sha256Hash":
          "aacdbed250e409105d124ea697ad291a06864c9343067714559fa01230c4cf1b",
        }
      },
    },
  ]

  response = requests.post(url, headers=headers, json=payload)

  data = response.json()

  # Obtém o JWT da extensionid "pm0qkv9g4h87t5y6lg329oam8j7ze9"
  for d in data:
    if "data" in d and "user" in d["data"] and "selfInstalledExtensions" in d[
        "data"]["user"]["channel"]:
      for ext in d["data"]["user"]["channel"]["selfInstalledExtensions"]:
        if ext["installation"]["extension"][
            "clientID"] == "pm0qkv9g4h87t5y6lg329oam8j7ze9":
          jwt = ext["token"]["jwt"]
          return jwt
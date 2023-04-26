# PCG-AUTO
Este é um bot criado em Python para a extensão Pokemon Community Game na plataforma Twitch.tv. Porém, como não sou especialista em programação, provalvemente há erros no código.

O bot tem a funcionalidade de capturar pokémons, desde que você tenha pokebolas ou pelo menos 300 de cash para comprá-las. O bot não é baseado em tier, e você pode personalizá-lo no arquivo main.py.

Para utilizá-lo, é necessário modificar algumas configurações nos arquivos:

Em main.py:

NICK: coloque o seu nome de usuário da Twitch.
PASS: insira o valor obtido em https://twitchapps.com/tmi como "oauth".
CHANNEL: insira o nome do canal que você está assistindo, como por exemplo "#2lives1stream".
Em obterjwt.py, na região "Authorization":
Troque o valor dentro de "OAuth xxxxxxxxxxxxxxxxxxxxxxxxx" pelo valor que você obteve seguindo os mesmos passos do vídeo abaixo . 

https://user-images.githubusercontent.com/84286668/234457032-1727f536-9d76-49cf-bac5-6fda3a653e13.mp4


O arquivo extras.txt contém um script para duelar automaticamente contra bots no estádio, no modo hard, selecionando movimentos aleatórios e trocando para pokémons aleatórios. Para executá-lo, clique com o botão direito do mouse em alguma região da extensão do Pokemon Community Game e abra o console developer tools, clique na aba Console e execute o script. Certifique-se de que no console você identificou "panel.html", caso contrário, o script não funcionará.
![image](https://user-images.githubusercontent.com/84286668/234454019-fcba05a4-1da5-415b-968b-777bf85a8a10.png)

Algumas informações relevantes:

O arquivo.py é responsável por obter suas pokebolas e itens do inventário.
O batalhaLista.py obterá os nomes e ids dos pokémons do seu time de batalha ativo.
O movesVerificar.py é responsável por obter os movimentos dos seus pokémons que estão no time de batalha ativo.
O nomePokemon.py está pegando o nome de um pokémon aleatório que será falado no chat a cada 15 minutos para receber dinheiro (o objetivo era evitar shadow ban).
O testes.py é o script responsável por comprar 1 pokebola.
O pokemon.py é responsável por obter algumas informações de seu pokémon, como nome, IV, base stats e preço.
O verificarPokemon.py é responsável por realizar trades de pokémons com o nome "trade" (está realizando o trade de um dos pokémons com nome "trade" e em seguida para o script por conta de algum erro que está acontecendo).

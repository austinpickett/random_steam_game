import random, requests, json, os
from dotenv import load_dotenv

def random_game():
  API_KEY = os.getenv('API_KEY')
  STEAM_ID = os.getenv('STEAM_ID')
  API_URL = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_KEY}&include_appinfo=true&steamid={STEAM_ID}&format=json'

  url = requests.get(API_URL)
  data = json.loads(url.text)

  game_list = list(map(lambda game: game["name"], data["response"]["games"]))

  print("You should play: " + random.choice(game_list))

if __name__ == '__main__':
  load_dotenv('.env')
  random_game()

import random, requests, json, os, webbrowser
from dotenv import load_dotenv


def random_game():
    API_KEY = os.getenv("API_KEY")
    STEAM_ID = os.getenv("STEAM_ID")
    API_URL = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_KEY}&include_appinfo=true&steamid={STEAM_ID}&format=json"

    url = requests.get(API_URL)
    data = json.loads(url.text)

    game_list = list(
        map(
            lambda game: {"name": game["name"], "appid": game["appid"]},
            data["response"]["games"],
        )
    )

    game = random.choice(game_list)

    print(f"You should play: {game['name']}")
    webbrowser.open(f"steam://store/{game['appid']}")


if __name__ == "__main__":
    load_dotenv(".env")
    random_game()

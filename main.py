
from http.client import responses
import requests
from pprint import pprint

def test_request():
    hero_dict = {}
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    for element in response.json():
        if element["name"] == 'Hulk' or element["name"] == "Captain America" or element["name"] == "Thanos":
            hero_dict[element["powerstats"]["intelligence"]] = element["name"]
            sorted(hero_dict.items())
    pprint(f'Самый умный герой: {list(hero_dict.values())[-1]}')    

if __name__ == '__main__':
    test_request()


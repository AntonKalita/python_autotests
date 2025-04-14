import requests
URL = 'https://api.pokemonbattle.ru'
TOKEN = '2782313637399a8163e472be3091dc6c'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
}
body_reqistration = {
    "name": "qenerate",
    "photo_id": 34
}

body_confirmation = {
    "pokemon_id": "288499",
    "name": "vova",
    "photo_id": 3
}

body_pokeboll = {
    "pokemon_id": "288499"
}

response = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_reqistration)
print(response.text)

response_confirmation = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)

response_pokeboll = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
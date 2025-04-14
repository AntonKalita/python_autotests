import requests 
import pytest 

URL = 'https://api.pokemonbattle.ru'
TOKEN = '2782313637399a8163e472be3091dc6c'
TRAINER_ID = '28595'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN 
}

def test_status_cod():
    response = requests.get(url = f'{URL}/v2/me', headers = HEADER)
    assert response.status_code == 200 
def test_trainer_name():
    response_get = requests.get(url = f'{URL}/v2/me', headers = HEADER)
    assert response_get.json()["data"][0]["trainer_name"] == 'Anton'

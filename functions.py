import json

import requests

URL = "https://viacep.com.br/ws/{}/json/"


def get_response_via_cep(cep_number):
    try:
        response = requests.get(URL.format(cep_number))
        if response.status_code == 200:
            return response.text

    except Exception as error:
        print(error)


def return_parsing_json(json_text):
    parsing = json.loads(json_text)
    return parsing


def returned_objects(parsing_response):
    cep = parsing_response['cep']
    address = parsing_response['logradouro']
    district = parsing_response['bairro']
    city = parsing_response['localidade']
    state = parsing_response['uf']
    return cep, address, district, city, state


def validation_cep(cep_number):
    try:
        cep_number = int(cep_number)
        cep_number = str(cep_number)
        if len(cep_number) == 8:
            return cep_number

        elif len(cep_number) <= 8:
            return 'Digite 8 números!'

        elif len(cep_number) >= 8:
            return 'Digite apenas 8 números!'

    except ValueError:
        return 'Digite apenas números!'

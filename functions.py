import json

import classe
import requests

brazilian_states = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}


def get_web_request_response(cep):
    return requests.get(f"https://viacep.com.br/ws/{str(cep)}/json/")


def get_json(web_request_response):
    return web_request_response.json()


def get_cep_number(json):
    return json["cep"]


def get_street(json):
    return json["logradouro"]


def get_district(json):
    return json["bairro"]


def get_city(json):
    return json["localidade"]


def get_state(json):
    return brazilian_states[json["uf"]]


def get_acronym(json):
    return json["uf"]


def get_font(font_name: str, font_size: int):
    font = classe.QFont()
    font.setFamily(font_name)
    font.setPointSize(font_size)
    return font


def create_label(window, x: int, y: int, width: int, height: int, style: str = None, font=None, margin: int = None):
    label = classe.QLabel(window)
    label.setGeometry(x, y, width, height)
    label.setStyleSheet(style)
    label.setFont(font)
    label.setMargin(margin)
    return label

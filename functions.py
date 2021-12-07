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
    return requests.get(f"https://viacep.com.br/ws/{cep}/json/")


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

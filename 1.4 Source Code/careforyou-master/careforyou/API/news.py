import requests


def get_news():
    API_KEY = '4dee0d3c2e486ff0d1c62e1e12782321'
    LANG = 'en'
    IMAGE = 'required'
    MAX_NUM = '3'
    KEY_WORD = 'childcare'
    response = requests.get(
        'https://gnews.io/api/v3/search?q='+KEY_WORD
        +'&max='+MAX_NUM
        +'&image='+IMAGE
        +'&language='+LANG
        +'&token='+API_KEY)
    return response.json()
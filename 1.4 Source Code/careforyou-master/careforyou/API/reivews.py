import requests
API_KEY = 'AIzaSyC43gZfAPsd-iyxc-2xEXsGHUJ1OdsTRJg'
URL_GET_PLACE = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?&inputtype=textquery'
URL_GET_REVIEWS = 'https://maps.googleapis.com/maps/api/place/details/json?'


def get_place_id(place):
    response = requests.get(
        URL_GET_PLACE +
        '&input=' + place +
        '&key=' + API_KEY
    )
    if response.json()['status'] == 'OK':
        try:
            return response.json()['candidates']
        except KeyError:
            pass
    return None


def get_reviews(place_id):
    response = requests.get(
        URL_GET_REVIEWS +
        'place_id=' + place_id +
        '&key=' + API_KEY
    )
    if response.json()['status'] == 'OK':
        try:
            return response.json()['result']['reviews']
        except KeyError:
            pass
    return None


if __name__ == '__main__':
    print(get_place_id('Altona Meadows Kindergarten, Victoria'))
    print(get_reviews('ChIJ9wHOuNmJ1moRLHUW6yiWcHk'))
import requests

def get_api(this_api):
    response = requests.get(this_api)
    return response

print(get_api('https://api.weather.gov'))
import requests
"""
headers = {
    'Host': 'hh.ru',
    "User-Agent": 'Chrome',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection':  'keep-alive'
}
"""
hh_requests = requests.get('https://hh.ru/search/vacancy?text=Python+junior&area=1')

print(hh_requests)
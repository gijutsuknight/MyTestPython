import requests

url = "https://itunes.apple.com/search?term=whatsapp&entity=software&country=us"
data = requests.get(url).json()
for app in data['results']:
    print(app['trackName'], app['sellerName'])

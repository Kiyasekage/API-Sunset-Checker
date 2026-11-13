import requests
param = [
    {'lat':36.72016 , 'lng': -4.42034}, #Malaga
    {'lat': -8.65000, 'lng': 115.21667} #Denpasar
]
for location in param:
    response = requests.get("https://api.sunrise-sunset.org/v2", params = location )
    data = response.json()
    print(data["sunset"])

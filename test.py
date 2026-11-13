import requests
param = [
    {'lat':36.72016 , 'lng': -4.42034}, #Malaga
    {'lat': -8.65000, 'lng': 115.21667} #Denpasar
]
print("Welcome to Sunset Checker for Malaga and Denpasar!")
ans = input("Do you want to check Malaga or Denpasar, or both?").lower()
if ans=="malaga":
    print(f"Malaga's sunset happens at {requests.get("https://api.sunrise-sunset.org/v2", params = param[0]).json()["sunset"]}") 
elif ans=="denpasar":
    print(f"Denpasar's sunset happens at {requests.get("https://api.sunrise-sunset.org/v2", params = param[1]).json()["sunset"]}")
elif ans=="both":
    for location in param:
        response = requests.get("https://api.sunrise-sunset.org/v2", params = location )
        data = response.json()
        print("Top is Malaga Bottom is Denpasar:\n",data["sunset"])
else:
    print("Wrong input!")

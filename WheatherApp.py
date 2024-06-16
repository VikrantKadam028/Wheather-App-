import requests
import json

print("***************************")
print("Welcome to Wheather App ⛅")
print("***************************")

city = input("Enter the name of the city :")
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(f"Temperature in {city}(Celcuis):{wdic["current"]["temp_c"]}")
print(f"Temperature in {city}(Fahraneits):{wdic["current"]["temp_f"]}")
print(f"Local time in {city}:{wdic["location"]["localtime"]}")
print(f"Humidity in {city}:{wdic["current"]["humidity"]}")


import requests

city_name=input("Enter city")
api_key="91030335dbc2ec4bd756a3e5fd685d50"
weather=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")

print(weather)


if weather.json()["cod"]=="404":
    print("Enter correct city name")
else:
    w=weather.json()["weather"][0]["main"]
    print(f"Waether of {city_name}is {w}")
    t=weather.json()["main"]["temp"]
    print(t)
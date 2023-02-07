import requests


response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=50.85&longitude=4.35&hourly=temperature_2m")
print(response.json()['hourly']['temperature_2m'])






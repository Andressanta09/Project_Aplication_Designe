import requests
import csv

# Fetch data from OpenWeatherMap
url = "https://api.openweathermap.org/data/2.5/weather?q=Toronto&appid=0daa089ec817d4921f4a1df8478dc369"
response = requests.get(url)
data = response.json()

# Print the data to inspect its structure
print(data)

# Write the data to a CSV if the expected keys exist
if 'name' in data and 'main' in data and 'wind' in data:
    with open('weather_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['City', 'Temperature (C)', 'Humidity', 'Wind Speed'])
        writer.writerow([data['name'], data['main']['temp'] - 273.15, data['main']['humidity'], data['wind']['speed']])
else:
    print("Expected keys not found in the response.")
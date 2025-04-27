import requests
from pprint import pprint

API_Key = '5be9ec2f20a42c801a00ede872a61e48'

city = input("Enter a city: ")

base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"

weather_data = requests.get(base_url).json()

if weather_data.get('cod') == 200:
    print(f"\nWeather Information for {weather_data['name']}, {weather_data['sys']['country']}:")
    print(f"Temperature     : {weather_data['main']['temp']}°C")
    print(f"Feels Like      : {weather_data['main']['feels_like']}°C")
    print(f"Humidity        : {weather_data['main']['humidity']}%")
    print(f"Pressure        : {weather_data['main']['pressure']} hPa")
    print(f"Weather         : {weather_data['weather'][0]['description'].title()}")
    print(f"Wind Speed      : {weather_data['wind']['speed']} m/s")
else:
    print(f"Error fetching weather data: {weather_data.get('message', 'Unknown error')}")

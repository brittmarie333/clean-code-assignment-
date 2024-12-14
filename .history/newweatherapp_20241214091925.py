#class for weather fetcher

class WeatherDataFetcher:

    def __init__(self):
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

        def fetch(self, city):
            print(f"Fetching weather for {city}")
            return self.weather_data(city,{})
        
#parse and format weather data
class DataParser:
    pass

    def parse(self, data):
        if not data:
            return "Invalid option, try again"
        
        city = data['city']
        temperature = data['temperature']
        condition = data['condition']
        humidity = data['humidity']
        return f"The weather in {city}: {temperature} degrees farenhiet, {condition}, {humidity}%"
    
#user interactions - ui
class UserInterface:

    def _
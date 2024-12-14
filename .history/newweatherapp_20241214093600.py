# Class for fetching weather data
class WeatherDataFetcher:

    def __init__(self):
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch(self, city):
        print(f"Fetching weather for {city}")
        return self.weather_data.get(city, None)


# Class to parse and format the weather data
class DataParser:

    def parse(self, data):
        if not data:
            return "Invalid option, try again"
        
        city = data['city']
        temperature = data['temperature']
        condition = data['condition']
        humidity = data['humidity']
        return f"The weather in {city}: {temperature} degrees Fahrenheit, {condition}, {humidity}% humidity."


#user interface UI
class UserInterface:

    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = DataParser()

    def get_user_info(self):
        city = input("Please provide the city you would like to view weather forecast or 'Exit' to quit: ")
        if city.lower() == 'exit':
            return None, None
        detailed = input("Would you like a detailed forecast? (yes/no): ").lower()
        return city, detailed
    
    def display(self, forecast):
        print(forecast)

    def get_detailed_forecast(self, city):
        data = self.fetcher.fetch(city)
        if not data:
            print("No weather forecast found!")
            return None
        weather_report = self.parser.parse(data)
        return weather_report

#main class to run the WeatherApp
class WeatherApp:

    def __init__(self):
        self.ui = UserInterface()

    def run(self):
        while True:
            city, detailed = self.ui.get_user_info()
            if city is None:
                print("Goodbye!")
                break
            if detailed == 'yes':
                forecast = self.ui.get_detailed_forecast(city)
            else:
                forecast = "Weather information available for " + city
            if forecast:
                self.ui.display(forecast)

if __name__ == '__main__':
    app = WeatherApp()
    app.run()

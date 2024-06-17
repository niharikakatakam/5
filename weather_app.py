import requests

def get_weather(api_key, location):
    """Fetch current weather data for the specified location using OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}  # You can change units to imperial for Fahrenheit

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        return weather_data
    except requests.exceptions.HTTPError as err:
        print(f"Error fetching weather data: {err}")
        return None

def display_weather(weather_data):
    """Display basic weather information."""
    if weather_data:
        print("\nCurrent Weather Information:")
        print(f"Location: {weather_data['name']}, {weather_data['sys']['country']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather Conditions: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to fetch weather data.")

def main():
    print("Welcome to the Weather App!")

    # Get user input for location
    location = input("Enter the city name or ZIP code: ")

    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '1037230343a4a42f996fa4114ae7729e'

    # Fetch weather data
    weather_data = get_weather(api_key, location)

    # Display weather information
    display_weather(weather_data)

if __name__ == "__main__":
    main()

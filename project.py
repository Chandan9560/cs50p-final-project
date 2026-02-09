import csv
import os
import requests


def main():
    # 1. Get user input (City name and Unit)
    city = input("What's your City? ").strip()
    unit = input("Display temperature in (C)elsius or (F)ahrenheit? ").strip().lower()

    # convert the unit for API
    unit = convert_unit(unit)

    # get weather data
    data = get_weather(city, unit)
    if data:
        raw_temp = data["main"]["temp"]
        pretty_temp = format_weather(raw_temp, unit)
        description = data["weather"][0]["description"]

        print(f"It is currently {description} with a temperature of {pretty_temp}")

        # save the history to file
        save_history(city, raw_temp, unit)
        print("Search saved to history!")
    else:
        print("City not found or connection error. Please try again.")


def convert_unit(unit):
    unit = unit.lower().strip()
    # handles just intial letter, short form, typo or full word.
    if unit in ["f", "far", "fahrenheit", "farenheit", "imperial"]:
        return "imperial"
    # default to celsius for everything else
    return "metric"


def get_weather(city, unit):
    # getting weather data from API
    API_KEY = "YOUR_API_KEY_HERE"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={unit}"

    # Return a dictionary of data
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.ResponseException:
        return None


def format_weather(temp, unit):
    # use f or c for output
    unit = "F" if unit == "imperial" else "°C"

    # Logic to add emojis and make it look pretty
    if unit == "F":
        if temp <= 32:
            return f"{temp}{unit} - Freezing! ❄️"
        elif 32 < temp <= 68:
            return f"{temp}{unit} - Chilly ☁️"
        elif 68 < temp <= 86:
            return f"{temp}{unit} - Pleasant ☀️"
        else:
            return f"{temp}{unit} - Very Hot! 🔥"

    else:
        if temp <= 0:
            return f"{temp}{unit} - Freezing! ❄️"
        elif 0 < temp <= 20:
            return f"{temp}{unit} - Chilly ☁️"
        elif 20 < temp <= 30:
            return f"{temp}{unit}- Pleasant ☀️"
        else:
            return f"{temp}{unit} - Very Hot! 🔥"


def save_history(city, raw_temp, unit):
    filename = "weather_history.csv"
    # check if file exists and not empty
    file_exists = os.path.isfile(filename) and os.path.getsize(filename) > 0

    unit = "F" if unit == "imperial" else "°C"

    # append the data to the csv file
    with open("weather_history.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["city", "temp", "unit"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({"city": city, "temp": raw_temp, "unit": unit})


if __name__ == "__main__":
    main()

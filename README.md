# Weather Tracker With History
#### Video Demo: [click here to watch the project video](https://youtu.be/yp5YS3dYau0)

#### Description:
This project is a robust, command-line interface (CLI) application developed as the final project for Harvard's CS50P. The primary goal of the application is to provide users with instantaneous weather data for any global city while maintaining a local, persistent record of their search habits. By integrating with the OpenWeatherMap API, the tool bridges the gap between simple local scripts and real-world web services.

#### Why I Built This:
I chose this project because it allowed me to practice four major pillars of Python programming: API interaction, data persistence with CSV files, error handling, and unit testing. I wanted to create a tool that wasn't just "run and forget," but something that built a database of information over time.

#### Detailed Features:
- **Real-Time API Integration:** The app uses the `requests` library to communicate with OpenWeatherMap. It handles the JSON response, parsing out specific data points like current temperature, humidity, and atmospheric conditions.
- **Defensive Input Parsing:** One of the main challenges was making the unit selection (Celsius vs. Fahrenheit) "bulletproof." I developed a function that uses string methods to interpret "c", "C", "Celsius", or even slight typos, ensuring the user experience isn't interrupted by strict input requirements.
- **Persistent Search History:** Every time a user successfully queries a city, the data—including a timestamp—is appended to `weather_history.csv`. I chose CSV over a standard text file to ensure the data could be easily exported to Excel or Google Sheets for later analysis.
- **User-Centric Visuals:** To make the terminal output less "boring," the application evaluates the temperature returned and assigns a specific emoji (like a sun or a snowflake) to give the user an immediate visual cue about the climate.

#### File Breakdown:
- `project.py`: This is the main executable. It contains the primary logic, including the API call functions and the CSV appending logic. I organized it so that the main logic is separated from the helper functions to keep the code clean and readable.
- `test_project.py`: Quality assurance is handled here. I wrote multiple test cases for each of my three required functions to ensure that no matter what the API returns, my conversion and formatting logic stays accurate.
- `requirements.txt`: This file ensures that any user can install the necessary dependencies (specifically the `requests` library) with a single command, making the project portable and easy to share.

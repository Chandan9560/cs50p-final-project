from project import convert_unit, format_weather


def test_convert_unit():
    # test common inputs
    assert convert_unit("f") == "imperial"
    assert convert_unit("Fahrenheit") == "imperial"
    assert convert_unit("c") == "metric"
    # test default input
    assert convert_unit("invalid_input") == "metric"


def test_format_weather_metric():
    # Test Celsius logic
    assert "Freezing" in format_weather(-5, "metric")
    assert "Chilly" in format_weather(15, "metric")
    assert "Pleasant" in format_weather(25, "metric")
    assert "Very Hot" in format_weather(35, "metric")


def test_format_weather_imperial():
    # Test Fahrenheit logic
    assert "Freezing" in format_weather(30, "imperial")
    assert "Chilly" in format_weather(55, "imperial")
    assert "Pleasant" in format_weather(75, "imperial")
    assert "Very Hot" in format_weather(100, "imperial")

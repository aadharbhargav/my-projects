import tkinter as tk
from tkinter import messagebox
import requests

# Replace this with your OpenWeatherMap API key
API_KEY = "a0f29d08a54fa3741e0056ec3b9f91fc"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data['main']['temp']
            weather = data['weather'][0]['description'].title()
            humidity = data['main']['humidity']
            wind = data['wind']['speed']

            result = f"Weather in {city.title()}\n\n"
            result += f"Temperature: {temp}°C\n"
            result += f"Condition: {weather}\n"
            result += f"Humidity: {humidity}%\n"
            result += f"Wind Speed: {wind} m/s"

            result_label.config(text=result)
        else:
            messagebox.showerror("Error", f"City not found: {city}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x350")
root.resizable(False, False)

font_style = ("Arial", 12)

# Widgets
tk.Label(root, text="Enter City Name:", font=font_style).pack(pady=10)
city_entry = tk.Entry(root, font=font_style, width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, font=font_style, bg="skyblue").pack(pady=10)

result_label = tk.Label(root, text="", font=font_style, justify="left")
result_label.pack(pady=20)

root.mainloop()

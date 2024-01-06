import tkinter as tk
import requests
import time
import config

def getWeather(canvas):
    latitude_and_longitude = textfield.get()
    latitude_and_longitude_list = latitude_and_longitude.split(",")
    latitude_raw = latitude_and_longitude_list[0]
    latitude = latitude_raw.strip()
    longitude_raw = latitude_and_longitude_list[1]
    longitude = longitude_raw.strip()
    api = "https://api.openweathermap.org/data/2.5/weather?lat=" + latitude + "&lon=" + longitude + "&" + config.api_key
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%M", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%H:%M:%M", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed" + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

g = ("poppins", 10,)
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

header = "Tom Bakers Weather App"
header1 = tk.Label(canvas, font = t)
header1.pack()
header1.config(text = header)

instructions = "To find out the weather at your chosen location, \n please enter coordinates as latitude,logitude \n (no spaces please and seperated by a , )"
instructions1 = tk.Label(canvas, font = g)
instructions1.pack()
instructions1.config(text = instructions)

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind("<Return>", getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()
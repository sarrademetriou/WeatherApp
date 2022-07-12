import tkinter as tk
import time
import requests
from PIL import ImageTk, Image
from dotenv import load_dotenv
import os 

def Configure():
    load_dotenv()
 
def Weather(root):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid={}".format(os.getenv('apikey'))
    json_data = requests.get(api).json()
    weather = json_data['weather'][0]['main']
    weathericon = json_data['weather'][0]['icon']
    img = Image.open("weathericons/{}.png".format(weathericon))
    newimg = ImageTk.PhotoImage(img)
 
    temp = int(json_data['main']['temp']-273.15) 
    temp_min = int(json_data['main']['temp_min']-273.15)
    temp_max = int(json_data['main']['temp_max']-273.15)
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    dawn = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise']+3600))
    dusk = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset']+3600))
    final_data = weather + "\n" + str(temp) + "°C" 
    final_extra_info = "Max Temp: " + str(temp_max) + "\n" + "Min Temp: " + str(temp_min) + "\n" + "Humidity: " + str(humidity) + "\n" + "Pressure: " + str(pressure)  + "\n" + "Wind Speed: " + str(wind) 
    sun_info = "\n" + "Sunrise: " + str(dawn) + "\n" + "Sunset: " + str(dusk)  

    label1.config(text = final_data)
    label2.config(text = final_extra_info)
    label3.config(text = sun_info)
    label4.config(image = newimg)
    label4.image = newimage 


root = tk.Tk()
title = root.title("Weather App!")
size = root.geometry("600x500")
f = ("poppins", 15, "bold")
t = ("poppins", 30, "bold")
textField = tk.Entry(root, justify='center', width = 20, font = t, fg = "#d2afff") 
textField.insert(0,"Enter any city!")

textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', Weather)
label1 = tk.Label(root, font=t, fg = "#5aa4e2")
label1.pack()
label4 = tk.Label(root, image ='')
label4.pack()
label2 = tk.Label(root, font=f, fg = "#74bbfb")
label2.pack()
label3 = tk.Label(root, font=f, fg = "#74bbfb")
label3.pack()

Configure()
root.mainloop()

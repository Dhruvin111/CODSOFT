from tkinter import *
import requests
import tkinter as tk

def get_weather():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f9755cd135771d1cee77d2e1ae8e740c").json()
    print(data)
    lbl_11.config(text=data["weather"][0]["main"])
    lbl_22.config(text=data["main"]["temp"])
    lbl_33.config(text=data["main"]["humidity"])
    lbl_44.config(text=data["weather"][0]["description"])

root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg='light gray')
city_name=tk.StringVar()

box = tk.Entry(root,textvariable=city_name)
box.place(x=100, y=50, height=30, width=200,)
box = tk.Label(root, text="Enter the city name:",font=("Times",15))
box.place(x=100, y=20)

lbl_1= Label(root,text="Climate:", font=("Times",15))
lbl_1.place(x=25, y=140, height=50, width=100)
lbl_11=Label(root,text=" ", font=("Times",15))
lbl_11.place(x=140, y=140,height=50, width=100)

lbl_2= Label(root,text="Temperature:", font=("Times",15))
lbl_2.place(x=25, y=200, height=50, width=105)
lbl_22=Label(root,text=" ", font=("Times",15))
lbl_22.place(x=140, y=200,height=50, width=100)
 
lbl_3= Label(root,text="Humidity:", font=("Times",15))
lbl_3.place(x=25, y=260, height=50, width=100)
lbl_33=Label(root,text=" ", font=("Times",15))
lbl_33.place(x=140, y=260,height=50, width=100)

lbl_4= Label(root,text="Description:", font=("Times",15))
lbl_4.place(x=25, y=320, height=50, width=100)
lbl_44=Label(root,text=" ", font=("Times",15))
lbl_44.place(x=140, y=320,height=50, width=100)

btn=Button(root, text="OK",command=get_weather)
btn.place(x=175,y=100, height=30, width=50)
root.mainloop()
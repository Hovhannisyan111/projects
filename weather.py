"""
This file is for showing weatherr data: 
Created by: Arman Hovhannisyan
Date: 29.04.2024
"""

import argparse
import requests
import json

def get_data(city):
    """
    Funnction: get_data
    Brief: sending a request to weeater site
    Params: city: city name of the input 
    Return: returns the list of dictionaries
    """

    key = ""
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city,
              "appid": key,
              "units": "metric"}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if response.status_code == 200:
            return data
    except Exception as e:
        print(e)
    

def get_arguments():
    """
    Function: get_ arguments
    Breif: parses argumments 
    return: returns city name and option
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--city", required=True, help="Input city name")
    parser.add_argument("-o", "--option", default="all", choices=["temp", "humidity", "pressure", "feel"], help="This is option")
    args = parser.parse_args()
    city = args.city
    option = args.option
    return city, option

def show_data(data, city, option):
    """
    Function: show_data
    Params: data: list of dicts, city: inputed city name, option: inpputed option
    Brief: prints all required data
    """
    name = data["name"]
    temp = data["main"]["temp"]
    feel = data["main"]["feels_like"]
    hum = data["main"]["humidity"]
    pres = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    
    if option == "all":
        print("City:", name)
        print(f"Temperature: {temp} C")
        print(f"Feels like: {feel} C")
        print(f"Humidity: {hum} %")
        print(f"Pressure: {pres} hPa")
        print(f"Wind speed: {wind}")
    elif option == "temp":
        print(f"Temperature: {temp} C")
    elif option == "feel":
        print(f"Feels like: {feel} C")
    elif option == "humidity":
        print(f"Humidity: {hum} %")
    elif option == "pressure":
        print(f"Pressure: {pres} HPA")
    

def main():
    """
    Function: main
    Breif: Entery point
    """
    city, option = get_arguments()
    data = get_data(city)
    if data:
        show_data(data, city, option)

if __name__ == "__main__":
    main()

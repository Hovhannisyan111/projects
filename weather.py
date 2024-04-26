import argparse
import requests
import json

def get_data(city):
    key = ""
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city,
              "appid": key,
              "units": "metric"}
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code == 200:
        return data
    
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--city", required=True, help="Input city name")
    parser.add_argument("-o", "--option", default="all", choices=["temp", "humidity", "pressure", "feel"], help="This is option")
    args = parser.parse_args()
    city = args.city
    option = args.option
    return city, option

def show_data(data, city, option):
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
    city, option = get_arguments()
    data = get_data(city)
    if data:
        show_data(data, city, option)
    else:
        print("No such city.")

if __name__ == "__main__":
    main()

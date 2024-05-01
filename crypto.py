"""
This file is for showing Crypto currence datas
Created by: Arman Hovhannisyan
Date: 30.04.2024
"""

import requests
import json
import time

def get_data():
    """
    Function: get_data
    Brief: The function sends a request to this api 
    Return: returns list of dictionaries conataining recieved data
    """
    url = "https://api.coincap.io/v2/assets"
    params = {"limit": 20}    
    try:
        response = requests.get(url, params=params)
        datas = response.json()
        if response.status_code == 200:
            return datas['data']
    except Exception as e:
        print(e)
    exit()

def filter_name(datas, name):
    """
    Function: filter_name
    Params: datas, name: name of the input
    Return: returns filterd list of dicts
    """
    return [i for i in datas if name.lower() in i["name"].lower()]

def filter_value(datas, value):
    """
    Function: filter_value
    Params: datas, value: inputed value to sort
    Resturn: filtered list of dictionaries
    """
    return [i for i in datas if float(i["priceUsd"]) > value]

def output_data(datas):
    """
    Function: output_data
    Brief: The funtion prints required data
    Params: datas
    """
    for data in datas:
        name = data['name']
        symbol = data['symbol']
        price = data['priceUsd']
        cup = data['marketCapUsd']
        vol = data['volumeUsd24Hr']
        per = data['changePercent24Hr']
        print(f"Name: {name}.")
        print(f"Symbol: {symbol}")
        print(f"Current Price: ${price}")
        print(f"Market cap: ${cup}")
        print(f"Total Volume: ${vol}")
        print(f"Price Change for 24 hours: {per}%")
        print("------------------------------------")

def main():
    """
    Function: main
    Brief: Entery point
    """
    while True:
       datas = get_data()
       output_data(datas)
       name = input("Enter a name to find: ")
       if name:
           data = filter_name(datas, name)
           output_data(data)
       value = input("Enter a value to sort by: ")
       if value.isdigit():
           data = filter_value(datas, float(value))
           output_data(data)
       time.sleep(5)
        
    
if __name__ == "__main__":
    main()


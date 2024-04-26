import requests
import json
import time

def get_data():
    url = "https://api.coincap.io/v2/assets"
    params = {"limit": 20}
    response = requests.get(url, params=params)
    datas = response.json()
    return datas['data']

def filter_name(datas, name):
    return [i for i in datas if name.lower() in i["name"].lower()]

def filter_value(datas, value):
    return [i for i in datas if float(i["priceUsd"]) > value]

def output_data(datas):
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


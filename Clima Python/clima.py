import requests
import json
from key import API_key


def city_data(API_key):
    print("\n======== APLICACION DEL CLIMA ========\n")
    while True:
        city_name = input("Ingrese el nombre de la ciudad de la cual desea saber el clima: ")
        url_api = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_key}"
        response = requests.get(url_api)
        if response.status_code == 200:
            response_json = response.json()
            if response_json:
                latitud = response_json[0]["lat"]
                longitud = response_json[0]["lon"]
                data = {"latitud" : latitud, "longitud" : longitud}
                return data
            else:
                print(f"la ciudad {city_name} no existe, intenta de nuevo.")
        else:
            print(f"no fue posible contactar con la API Error: {response.status_code}")

def city_weather(API_key, data):
    url_api = f"https://api.openweathermap.org/data/2.5/weather?lat={data["latitud"]}&lon={data["longitud"]}&appid={API_key}&&lang=es"
    response = requests.get(url_api)
    if response.status_code == 200:
        response_json = response.json()
        if response_json:
            print(f"\nInformacion del clima en la ciudad de {response_json["name"]}, {response_json["sys"]["country"]}:\n")
            print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
            print(f"| Temperatura : {response_json["main"]["temp"] - 273.15:.2f}° Celsius                   |")
            print(f"| Se sienten: {response_json["main"]["feels_like"] - 273.15:.2f}° Celsius                      |")
            print(f"| Temperatura Max & Min: {response_json["main"]["temp_max"] - 273.15:.2f}° & {response_json["main"]["temp_min"] - 273.15:.2f}° Celsius |")
            print(f"| Presion: {response_json["main"]["pressure"]} hPa.                             |")
            print(f"| Humedad: {response_json["main"]["humidity"]}%                                   |")
            print(f"| Velocidad del viento: {response_json["wind"]["speed"]} M/s                 |")
            print(f"| Descripcion del clima: {response_json["weather"][0]["description"]}                   |")
            print("|________________________________________________|")

        else:
            print(f"No hay ninuna inofrmacion para las coodernadas | Latitud: {data["latitud"]} | Longitud: {data["longitud"]} |")
    else:
        print(f"no fue posible contactar con la API Error: {response.status_code}")

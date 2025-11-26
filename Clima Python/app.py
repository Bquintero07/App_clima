from clima import city_data, city_weather, API_key


data = city_data(API_key)
city_weather(API_key, data)
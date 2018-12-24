import urllib.request
import gzip
import os
import json
import sqlite3
import requests
import time
import datetime

appid = '0bfd5ecb59cad4d4c2c8a3423db6b2d5'

  
def country_list(list_data): # создание списка стран (все страны не перебираю)
    country_list = []
    n = 0
    for i in list_data:
        info = Country_list(list_data[list_data.index(i)])
        country_list.append(info.country)
        country_list_true = set(country_list)
        n +=1
        if n > 100:
            break
    print(country_list_true)
    
def city_list(list_data, country_name): #создание списка 20 первых городов
    city_list = {}
    n = 0
    for i in list_data:
        info = Country_list(list_data[list_data.index(i)])
        if info.country == country_name:
            city_list[n] = info.name
            n +=1
            if n > 20:
                break
    print(city_list)
    return city_list


   
def city_id(list_data, city_name): # получение ID
    n = 0
    for i in list_data:
        info = Country_list(list_data[list_data.index(i)])
        if info.name == city_name:
            break
    return info.id

def forecast(s_city, city_name, appid): # погода в городе
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                params={'id': s_city, 'type': 'like', 'units': 'metric','lang': 'ru', 'APPID': appid})
    data = res.json()
    print("погода в городе %s" % city_name) 
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
    print("weather id:", data['weather'][0]['id'])
    data  = time.ctime(data['dt'])
    print("date:", data)
    temp = data['main']['temp']
    weatherid = data['weather'][0]['id']
    
    return temp, data, weatherid

def forecast_file_table(city_name, cityid, data, temp, weatherid): # создание файла с базой погоды
    conn = sqlite3.connect("data\%s forecast.db" % city_name) 
    cursor = conn.cursor()
 
    cursor.execute("""CREATE TABLE forecast
                  (id_города INTEGER PRIMARY KEY, Город VARCHAR(255), Дата DATE,
                   Температура INTEGER, id_погоды INTEGER)
               """)
    cursor.execute("""INSERT INTO forecast
                  VALUES ('cityid', 'city_name', 'data',
                  'temp', 'weatherid')"""
                   )
    conn.commit()    

class Country_list:
    def __init__(self, d):
        for a, b in d.items():
            setattr(self, a, b)
            
def creating_data_fromOW(date): # получение и создание базы городов с сайта openweather
    if os.path.exists("data\\%scity.list.json.gz" % date):
         print ("Файл за дату %s уже сгенерирован продолжаем)" % date)
    else:
        dw_file = urllib.request.urlopen("http://bulk.openweathermap.org/sample/city.list.json.gz")
        output = open('data\%scity.list.json.gz' % date,'wb')
        output.write(dw_file.read())
        output.close()

        inF = gzip.open("data\%scity.list.json.gz" % date, 'rb')
        outF = open("data\%scity.list.json" % date, 'wb')
        outF.write( inF.read() )
        inF.close()
        outF.close()
        
def main():
    d = datetime.date(2018, 12, 24)
    date= str(d.day) + str(d.month) + str(d.year)
    creating_data_fromOW(date)
        
    with open("data\%scity.list.json" % date, 'r', encoding='UTF-8') as f:
        read_data = json.load(f)
        country_list(read_data)
        country  = input('Введите название страны из примера выше - ')
        city_list_data = city_list(read_data, country)
        city_name_num = input("введите номер города в котором вы хотите узнать погоду\n выводим список  первых 20 городов - ")
        city_name = city_list_data[int(city_name_num)]
        s_city = city_id(read_data, city_name)
        forecast(s_city,city_name, appid)
        cityid = info.id
        forecast_file_table(city_name, info.id, data, temp, weatherid)

if __name__ == "__main__":
    main()

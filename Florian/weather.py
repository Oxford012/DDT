import pandas as pd

# method to get the clean weather data from the csv file
# from weather import getCleanWeather
def getCleanWeather(pathToWeatherCSV):
    weather = pd.read_csv(pathToWeatherCSV)
    weather['timestamp'] = pd.to_datetime(weather['timestamp'])
    weather = weather[(weather['timestamp'].dt.year >= 2017) & (weather['timestamp'].dt.year <= 2018)]
    weather.reset_index(drop=True, inplace=True)
    weather = weather.dropna(axis=0, how='any')
    return weather


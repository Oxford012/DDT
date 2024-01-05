import numpy as np
import pandas as pd

def clean_data(pathToData):
    bluebikes = pd.read_csv(pathToData)
    bluebikes["start_time"] = pd.to_datetime(bluebikes["start_time"])
    bluebikes["end_time"] = pd.to_datetime(bluebikes["end_time"])

    # adding weekdays
    bluebikes['weekday'] = bluebikes['start_time'].dt.weekday

    # sort the values by start time
    bluebikes.sort_values(["start_time"], inplace=True)
    #remove unnamed: 0 column
    bluebikes.drop(bluebikes[bluebikes['end_time'] < bluebikes['start_time']].index, inplace=True)
    bluebikes.drop(bluebikes[(bluebikes['start_time'].dt.year < 2017) | (bluebikes['start_time'].dt.year > 2018)].index, inplace=True)
    bluebikes.drop(bluebikes[(bluebikes['end_time'].dt.year < 2017) | (bluebikes['end_time'].dt.year > 2018)].index, inplace=True)
    
    # reset the index and drop the existing index column
    bluebikes.reset_index(drop=True, inplace=True)

    return bluebikes


def new_clean_data(pathToData):
    bluebikes = pd.read_csv(pathToData)
    bluebikes["start_time"] = pd.to_datetime(bluebikes["start_time"])
    bluebikes["end_time"] = pd.to_datetime(bluebikes["end_time"])

    # adding weekdays
    bluebikes['weekday'] = bluebikes['start_time'].dt.weekday

    # sort the values by start time
    bluebikes.sort_values(["start_time"], inplace=True)
    bluebikes.drop(bluebikes[bluebikes['end_time'] < bluebikes['start_time']].index, inplace=True)
    bluebikes.drop(bluebikes[(bluebikes['start_time'].dt.year < 2017) | (bluebikes['start_time'].dt.year > 2018)].index, inplace=True)
    bluebikes.drop(bluebikes[(bluebikes['end_time'].dt.year < 2017) | (bluebikes['end_time'].dt.year > 2018)].index, inplace=True)

    
    # remove values with bad coordinates
    outlier_cords = [(0.0, 0.0), (-90.0,0.0), (45.505086, -73.566921), (42.16722555541654, -70.90555783370291)]
    for point in outlier_cords:
        bluebikes = bluebikes[~((bluebikes.start_station_lat == point[0]) & (bluebikes.start_station_lon == point[1]))]
        bluebikes = bluebikes[~((bluebikes.end_station_lat == point[0]) & (bluebikes.end_station_lon == point[1]))]

    # remove unnecessary columns
    bluebikes.drop(['Unnamed: 0'], axis=1, inplace=True)
    bluebikes.drop(['start_station_lat'], axis=1, inplace=True)
    bluebikes.drop(['start_station_lon'], axis=1, inplace=True)    
    bluebikes.drop(['end_station_lat'], axis=1, inplace=True)    
    bluebikes.drop(['end_station_lon'], axis=1, inplace=True)        

    # reset the index and drop the existing index column
    bluebikes.reset_index(drop=True, inplace=True)
    return bluebikes



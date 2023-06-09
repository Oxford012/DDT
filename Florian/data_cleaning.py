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
    bluebikes.drop(bluebikes[bluebikes['end_time'] < bluebikes['start_time']].index, inplace=True)
    bluebikes.drop(bluebikes[(bluebikes['start_time'].dt.year < 2017) | (bluebikes['start_time'].dt.year > 2018)].index, inplace=True)
    bluebikes.drop(bluebikes[(bluebikes['end_time'].dt.year < 2017) | (bluebikes['end_time'].dt.year > 2018)].index, inplace=True)

    return bluebikes
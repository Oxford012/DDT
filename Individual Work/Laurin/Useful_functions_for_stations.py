import pandas as pd
import folium


def map_stations_all_cords(data):
    bluebikes_start_stations_map_points = folium.Map(location=(42.361145, -71.057083), tiles="OpenStreetMap",
                                                     zoom_start=12)

    # draw positions for the stations
    # whether we choose the coordinates from start or end station does not matter since they are the same
    # i want a red icon
    for key, value in data.items():
        color = ['red', 'green', 'blue', 'orange', 'white']
        i = 0
        for point in value:
            folium.Marker(location=point, icon=folium.Icon(color=color[i]),
                          popup=(str(key) + "\n" + str(point))).add_to(bluebikes_start_stations_map_points)
            i += 1

    return bluebikes_start_stations_map_points


def map_stations_with_multiple_coordinates(data):
    bluebikes_start_stations_map_points = folium.Map(location=(42.361145, -71.057083), tiles="OpenStreetMap",
                                                     zoom_start=12)

    # draw positions for the stations
    # whether we choose the coordinates from start or end station does not matter since they are the same
    # i want a red icon
    for key, value in data.items():
        if (len(value) > 1):
            color = ['red', 'green', 'blue', 'orange', 'white']
            i = 0
            for point in value:
                folium.Marker(location=point, icon=folium.Icon(color=color[i]),
                              popup=(str(key) + "\n" + str(point))).add_to(bluebikes_start_stations_map_points)
                i += 1

    return bluebikes_start_stations_map_points

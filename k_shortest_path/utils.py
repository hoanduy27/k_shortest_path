import numpy as np

EARTH_RADIUS = 6371

def dist(long1, lat1, long2, lat2):
    np.arccos(
        np.sin(lat1)*np.sin(lat2)
        + np.cos(lat1)*np.cos(lat2)*np.cos(long2-long1)
    )*EARTH_RADIUS

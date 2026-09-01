import numpy as np

def solution_station_6(station6):
  radians = np.deg2rad(station6) 
  result = np.sin(radians)
  return round(result, 4)
#might not need the 4
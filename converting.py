#to check how to convert address to laptitude and longtitude

import pandas,geopy
from geopy.geocoders import ArcGIS
arcgis= ArcGIS()

dataFrame = pandas.read_csv("examplefile1.csv")
a=dataFrame["address"].apply(arcgis.geocode)
dataFrame["Longitude"] = a.apply(lambda loc: loc.longitude if loc != None else None)
dataFrame["Latitude"] = a.apply(lambda loc: loc.latitude)

print(dataFrame)
dataFrame.to_csv("examplefile1.csv")

from math import radians, cos, sin, asin, sqrt
# Distance between two lat/lng coordinates in km using the Haversine formula
def getDistanceFromLatLng(lat1, lng1, lat2, lng2, miles=False): # use decimal degrees
  r=6371 # radius of the earth in km
  lat1=radians(lat1)
  lat2=radians(lat2)
  lat_dif=lat2-lat1
  lng_dif=radians(lng2-lng1)
  a=sin(lat_dif/2.0)**2+cos(lat1)*cos(lat2)*sin(lng_dif/2.0)**2
  d=2*r*asin(sqrt(a))
  if miles:
    return d * 0.621371 # return miles
  else:
    return d # return km
# Copyright 2016, Chris Youderian, SimpleMaps, http://simplemaps.com/resources/location-distance
# Released under MIT license - https://opensource.org/licenses/MIT

# Test data
# 46635 South Bend  41.708505,-86.20906
# 46516 Elkhart     41.676899,-85.96044
lat1 = 41.708505
lng1 = -86.20906
lat2 = 41.676899
lng2 = -85.96044

dst = getDistanceFromLatLng(lat1,lng1,lat2,lng2,True)
print (dst)

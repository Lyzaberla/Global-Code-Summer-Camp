#for address and coordinates
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='DistApp')
def distance():
    location1 =input('enter any city/country name')
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent='DistApp')
    location = geolocator.geocode(location1)
    print("the address of", location1, "is:", location.address)
    print('the longitude and latitude of',location1, 'is:', (location.latitude, location.longitude))
    length1=location.longitude
    width1 =location.latitude
    
    location2=input('enter another city/country name')
    location = geolocator.geocode(location2)
    print("the address of", location2, "is:", location.address)
    print('the longitude and latitude of',location2, 'is:', (location.latitude, location.longitude))
    length2=location.longitude
    width2 =location.latitude
    
    from geopy.distance import geodesic
    location_a = (length1, width1)
    location_b = (length2, width2)
    print('The distance between',location1,'and',location2,'is',geodesic(location_a, location_b).miles ,'miles')


    
#print(location.raw)

'''location = geolocator.reverse("52.509669, 13.376294")
print(location.address)
print((location.latitude, location.longitude))
#print location raw

#distance between two cities
    #using great circle
from geopy.distance  import great_circle
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(great_circle(newport_ri, cleveland_oh).miles)'''

def main():
    distance()
    
    
main()
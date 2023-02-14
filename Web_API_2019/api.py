import pyowm
 
owm = pyowm.OWM('e5581033c1d27f30811470eed6982628')
observation = owm.weather_at_place('Cape Coast, Ghana')
w = observation.get_weather()
 
print(w.get_wind())
print(w.get_humidity())
import pywapi as weather
import phue

'''Get chance of precipitation for current day'''
current = weather.get_weather_from_weather_com('10023', units='imperial')
precip = current['forecasts'][0]['day']['chance_precip']

'''Set hue light if it gon rain'''
if precip >= "30":
	b = phue.Bridge('192.168.1.120')
	b.connect()
	b.get_api()
	b.set_light(9, 'bri', 254)
	b.set_light(9, 'hue', 46920)
	b.set_light(9, 'sat', 255)
	b.set_light(9, 'on', True)
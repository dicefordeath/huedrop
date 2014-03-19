import pywapi as weather
import phue

'''Get chance of precipitation for current day'''
current = weather.get_weather_from_weather_com('10023', units='imperial')
precip = current['forecasts'][0]['day']['chance_precip']

'''Set hue light accordingly'''
b = phue.Bridge('192.168.1.1')
b.connect()
b.get_api()
b.set_light(4, 'on', True)
b.set_light(4, 'bri', 254)
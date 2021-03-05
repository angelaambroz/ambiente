#!/usr/bin/env python3

import time
from datetime import datetime

from ltr559 import LTR559
from bme280 import BME280

ltr = LTR559()  
bme = BME280()

try:
    while True:
        today = datetime.now().strftime('%Y-%m-%d %H:%S')

        ltr.update_sensor()

        # https://en.wikipedia.org/wiki/Lux
        # https://www.youtube.com/watch?v=mW6QLkR9ibQ
        # "how much light hits the surface"
        lux = ltr.get_lux()

        # https://github.com/pimoroni/ltr559-python/issues/3 
        # We have no idea what the units are
        # https://optoelectronics.liteon.com/upload/download/DS86-2013-0003/LTR-559ALS-01_DS_V1.pdf
        # It's a light sensor - it senses reflected light from objects 
        # https://en.wikipedia.org/wiki/Proximity_sensor
        # https://www.youtube.com/watch?v=QfQ_bL8AeGo
        prox = ltr.get_proximity()

        # https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout?view=all
        # Official docs: https://www.bosch-sensortec.com/media/boschsensortec/downloads/product_flyer/bst-bme280-fl000.pdf
        # it's celsius
        temp = bme.get_temperature()

        # https://en.wikipedia.org/wiki/Pascal_(unit)
        # 1 hectopascal (hPa) = 100 Pa
        # https://www.sensorsone.com/hpa-hectopascal-pressure-unit/
        # the international standard for measuring atmospheric/barometric pressure
        # https://www.youtube.com/watch?v=DquXO2FEl0Q
        # https://www.youtube.com/watch?v=pTILmF-sx9w low pressure = rain? high pressure = dry?
        pres = bme.get_pressure()

        # https://en.wikipedia.org/wiki/Humidity
        # https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout?view=all
        # Relative humidity: "expressed as a percentage, indicates a present state of absolute humidity relative to a maximum humidity given the same temperature" (wiki)
        hum = bme.get_humidity()
    
        readings_message = f'''
               {today}
               Temperature:\t{temp:.1f} C
               Pressure:\t{pres:.2f} hPa
               Humidity:\t{hum:.0f}%
               Light:\t\t{lux:.2f} Lux
               Proximity:\t{prox:.2f} reflected Lux (?)
               \n
               '''

        print(readings_message)

        time.sleep(1)

except KeyboardInterrupt:
    pass

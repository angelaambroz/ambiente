#!/usr/bin/env python3

import time
import csv
from datetime import datetime

from ltr559 import LTR559
from bme280 import BME280

ltr = LTR559()  
bme = BME280()

header = ['datetime', 'light', 'proximity', 'temperature', 'humidity']
data_file = 'data/kitchen.csv'

try:

    # Write the header once
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)

    while True:
        f = open(data_file, 'a')
    
        writer = csv.writer(f)

        today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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

        writer.writerow([today, f"{lux:.2f}", f"{prox:.2f}", f"{temp:.2f}", f"{hum:.2f}"])

        time.sleep(60)
        f.close()

except KeyboardInterrupt:
    pass

#!/usr/bin/env python3

import time
from ltr559 import LTR559
from bme280 import BME280

ltr = LTR559()  
bme = BME280()

try:
    while True:
        ltr.update_sensor()
        lux = ltr.get_lux()
        prox = ltr.get_proximity()
        temp = bme.get_temperature()
        pres = bme.get_pressure()
        hum = bme.get_humidity()
    
        readings_message = f'''
               Temperature:\t{temp:.1f} C
               Pressure:\t{pres:.2f}
               Humidity:\t{hum:.0f}%
               Light:\t\t{lux:.2f} ...luxes?
               Proximity:\t{prox:.2f} ...proxes?
               \n
               '''

        print(readings_message)

        time.sleep(1)

except KeyboardInterrupt:
    pass

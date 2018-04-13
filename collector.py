#!/usr/bin/env python3

import bme680
import time
from event import Event
from event import EventType as etype
from event import Threshold as threshold

print("""Estimate indoor air quality
Runs the sensor for a burn-in period, then uses a
combination of relative humidity and gas resistance
to estimate indoor air quality as a percentage.
Press Ctrl+C to exit
""")

sensor = bme680.BME680()
DEBUG=True
EVENT=True
event = Event()
# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

# start_time and curr_time ensure that the
# burn_in_time (in seconds) is kept track of.

start_time = time.time()
curr_time = time.time()
if (DEBUG):
    burn_in_time=20
else:
    burn_in_time = 300

burn_in_data = []

try:
    # Collect gas resistance burn-in values, then use the average
    # of the last 50 values to set the upper limit for calculating
    # gas_baseline.
    print("Collecting gas resistance burn-in data for {0} mins\n".format(burn_in_time/60))
    while curr_time - start_time < burn_in_time:
        curr_time = time.time()
        if sensor.get_sensor_data() and sensor.data.heat_stable:
            gas = sensor.data.gas_resistance
            burn_in_data.append(gas)
            print("Gas: {0} Ohms".format(gas))
            time.sleep(1)

    gas_baseline = sum(burn_in_data[-50:]) / 50.0

    # Set the humidity baseline to 40%, an optimal indoor humidity.
    hum_baseline = 40.0

    # This sets the balance between humidity and gas reading in the
    # calculation of air_quality_score (25:75, humidity:gas)
    hum_weighting = 0.25

    print("Gas baseline: {0} Ohms, humidity baseline: {1:.2f} %RH\n".format(gas_baseline, hum_baseline))

    while True:
        if sensor.get_sensor_data() and sensor.data.heat_stable:
            if EVENT:
                if(DEBUG):
                    print("[DEBUG] gas: {0} ".format(sensor.data.gas_resistance))
                    print("[DEBUG] humidity: {0} ".format(sensor.data.humidity))
                    print("[DEBUG] temp: {0} ".format(sensor.data.temperature))
                if (sensor.data.gas_resistance >= threshold.gas):
                    event.trigger(sensor.data, etype.GAS)
                if (sensor.data.humidity >= threshold.humidity):
                    event.trigger(sensor.data, etype.HUMIDITY)
                if not (threshold.temperature[0] <= sensor.data.temperature <= threshold.temperature[1]):
                    event.trigger(sensor.data, etype.TEMPERATURE)

                print()
                print("DONE...")
                print()
            time.sleep(1)

except KeyboardInterrupt:
    pass

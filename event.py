from enum import Enum


class EventType(Enum):
     GAS = 1
     HUMIDITY = 2
     PRESSURE = 3
     TEMPERATURE = 4

class Event(object):
    def trigger(self, data, type):
        if type == EventType.GAS:
            self._trigger_gas_event(data)
        elif type == EventType.HUMIDITY:
            self._trigger_hum_event(data)
        elif type == EventType.TEMPERATURE:
            self._trigger_temp_event(data)
        elif type == EventType.PRESSURE:
            return

    def _trigger_gas_event(self, data):

        print ("\tGas threshold {0} exceeded: ({1:.2f})".format(Threshold.gas, data.gas_resistance))

    def _trigger_hum_event(self, data):
        print ("\tHumidity threshold {0} exceeded: ({1:.2f})".format(Threshold.humidity, data.humidity))

    def _trigger_temp_event(self, data):
        print ("\tTemperature threshold {0} exceeded: ({1:.2f})".format(Threshold.temperature, data.temperature))

class Threshold(object):
    gas = 230000
    humidity = 50
    temperature = [22.50, 24]

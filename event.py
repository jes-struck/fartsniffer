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

    def _trigger_gas_event(data):
        print ("\tGetting gas_resistance: ({0})".format(data.gas_resistance))
        print()
        print("DONE...")
        print()

    def _trigger_hum_event(data):
        print ("\tGetting humidity: ({0})".format(data.humidity))
        print()
        print("DONE...")
        print()

    def _trigger_temp_event(data):
        print ("\tGetting temperature: ({0})".format(data.temperature))
        print()
        print("DONE...")
        print()

class Threshold(object):
    gas = 350000
    humidity = 50
    temperature = [18,24]


class EventType(Enum):
     GAS = 1
     HUMIDITY = 2
     PRESSURE = 3

class Event(object):

    def trigger(date, type):
        slef.data = data
        print ("\tGetting status: ({0})".format(data.status))            #data.status
        print ("\tGetting gas_index: ({0})".format(data.gas_index)) #gas_index
        print ("\tGetting meas_index: ({0})".format(data.meas_index)) #meas_index
        print ("\tGetting temperature: ({0})".format(data.temperature)) #temperature
        print ("\tGetting pressure: ({0})".format(data.pressure)) #pressure
        print ("\tGetting humidity: ({0})".format(data.humidity)) #humidity
        print ("\tGetting gas_resistance: ({0})".format(data.gas_resistance)) #gas_resistance
        print()
        print("DONE...")
        print()

    """docstring for [object Object]."""
    def __init__(self, arg):
        super([object Object], self).__init__()
        self.arg = arg

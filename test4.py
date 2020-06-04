from datetime import datetime         # import the module
import serial           # import the module
import time             # import the module


def get_time():
    c = datetime.now()
    hour = str(c.hour)
    minute = str(c.minute)
    second = str(c.second)
    if len(hour) == 1:
        hour = '0' + hour

    if len(minute) == 1:
        minute = '0' + minute

    if len(second) == 1:
        second = '0' + second

    return hour + minute + second

# sending data

ComPort = serial.Serial('COM7') # open COM24
ComPort.baudrate = 9600 # set Baud rate to 9600
ComPort.bytesize = 8    # Number of data bits = 8
ComPort.parity   = 'N'  # No parity
ComPort.stopbits = 1    # Number of Stop bits = 1

#time_str = get_time()

for i in range(10):
    time_str = get_time()
    print(time_str)
    data = bytearray(time_str,'utf-8')
    No = ComPort.write(data)
    #dat = ComPort.read(6)   # Wait and read data
    #print(dat)              # print the received data
    time.sleep(4)
    

ComPort.close()         # Close the Com port

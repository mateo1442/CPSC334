import serial

ser = serial.Serial()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 9600
ser.setDTR(False)
ser.setRTS(False)

ser.open()

while(True):
    b = ser.readline()
    print(b)
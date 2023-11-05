import serial

arduino = serial.Serial("/dev/tty/ACM", 9600)  # Replace 'COMX' with the correct serial port name

with open('temperature_data.txt', 'w') as file:
    while True:
        data = arduino.readline().decode('utf-8')
        file.write(data)
        print(data, end='') 
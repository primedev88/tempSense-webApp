import serial.tools.list_ports
import json

ports = serial.tools.list_ports.comports()
serialInst=serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

serialInst.baudrate = 9600
serialInst.port = "COM3"
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        numbers=[float(num) for num in packet.split()]
        data = {
            "Temperature": numbers[0],
            "Voltage": numbers[1],
            "Resistance": numbers[2]
        }
        with open('dataset.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        

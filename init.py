import serial.tools.list_ports

old_List = list()

while True:
    list = serial.tools.list_ports.comports()

    if(len(old_List) < len(list)):
        for element in list:
            print(element.device)

        old_List = list
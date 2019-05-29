import serial
ser = serial.Serial("COM5", 115200)
ser.write("<<SENDFILE>>\n")
readline = lambda : iter(lambda:ser.read(1), '\n')
with "".join(readline()) != "<<SENDFILE>>":
    pass
ser.write(open("latlng.txt", "rb").read())
ser.write("\n<<EOF>>\n")

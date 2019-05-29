f = open("D:\\home\\hacktj\\latlng.txt", "w+")

i = [38.8834,
-77.1028
]
for c in i:
    f.write(str(c))
    f.write('\n')
f.close()
print(type(i))
##

import serial
ser = serial.Serial('COM3', 38400)  # open serial port
print(ser.name)         # check which port was really
ser.write(b'hello')     # write a string
ser.close()

##

import sys

for line in sys.stdin:
    print(line)
    
    ##
f = open("D:\\home\\hacktj\\info.txt", "w+")
f.write(input("Enter yuour name: "))

f.close()
##
f = open('D:\\home\\hacktj\\info.txt', 'w+')
f.write(input('Enter your name: ')+'\n')
f.write(input('Enter your age: '))
f.write(input('Enter your gender (0 for male; 1 for female): '))
f.close()


f = open('info.txt', 'w+')
f.write(input('Enter your name: ')+'\n')
f.write(input('Enter your age: ')+'\n')
f.write(input('Enter your gender (0 for male; 1 for female): ')+'\n')
f.write(input('Enter your address: ) + '\n')
f.close()

##

lat = 38.8834
lng = -77.1028
#check 5 min 
for i in range(5):
    time.sleep(1)
    print(4)
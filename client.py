import time
import datetime



f = open('D:\\home\\hacktj\\info.txt', 'a')

f.write(str(time.time())+'\n')
f.write(datetime.date.today().strftime("%W")+'\n')

f.write(datetime.date.today().strftime("%w")+'\n')

f.close()


from serial import Serial
ser = Serial('COM5', 9600) #or whatever 
ser.write("<<SENDFILE>>\n") #tell server we are ready to recieve
readline = lambda : iter(lambda:ser.read(1),"\n")
with open("latlng.txt","wb") as outfile:
   while True:
       line = "".join(readline())
       if line == "<<EOF>>":
           break #done so stop accumulating lines
       print >> outfile,line
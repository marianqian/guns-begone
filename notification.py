f = open('D:\\home\\hacktj\\latlng.txt', 'r')

lat = float(f.readline())
lng = float(f.readline())

school_lat = 38.81695
school_lng = -77.16785


##
#!/usr/bin/env python
# Import smtplib for the actual sending function

import smtplib
from email.mime.text import MIMEText
msg = MIMEText("WARNING: A person in possession of a firearm has entered the proximity. Serial Number: 0000")
msg['Subject'] = "GUN WARNING"
msg['From'] = "mqian36@gmail.com"
msg['To'] = "7037313727@messaging.sprintpcs.com"
s = smtplib.SMTP('localhost')
s.set_debuglevel(1)
s.sendmail(msg['From'], [msg['To']], msg.as_string())
s.quit()
print("Text sent!")

##
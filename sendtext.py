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

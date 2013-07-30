import subprocess as sub
import os
import sys
import time
import smtplib
from email.mime.multipart import MIMEMultipart

def ServiceCheck(ServiceToCheck):
    service = ServiceToCheck
    command = 'SC query '+ service +' | find "STATE"'
    restart = 'SC start '+ service
    i=1

    from_address = ''
    receivers = ['', '']    
    s = smtplib.SMTP('')

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = ", ".join(receivers)   

    while i < 3:
        p = os.popen(command,"r")
        line = p.readline()
        if line.find('RUNNING') != -1:
            failed = "no"
            break
        else:
            sub.call (restart)
            time.sleep(10)
            i=i+1
            failed = "yes"
            if i == 2:
                # Build the email
                msg['Subject'] = 'The '+service+' service is Stopped, attempting restart...'         
                # Send the email via SMTP server.
                s.send_message(msg)
                s.quit()
            
    if failed == "yes":
        # Build the email
        msg['Subject'] = 'The '+ service +' service has stopped working.'         
        # Send the email via SMTP server.
        s.send_message(msg)
        s.quit()
            
for s in sys.argv[1:]:
    ServiceCheck(s)

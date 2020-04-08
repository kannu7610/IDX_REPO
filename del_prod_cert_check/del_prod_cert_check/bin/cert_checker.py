import os
from datetime import date
import time

#today = date.today()


with open('/opt/splunk/etc/apps/del_prod_cert_check/bin/certfiles.txt','w') as file_write:
    cert = 'find /opt/splunk/ -type f -name *.pem | grep -i "del_"'
    cert_lines = os.popen(cert).read()
    file_write.write(cert_lines)

try :
    with open('/opt/splunk/etc/apps/del_prod_cert_check/bin/certfiles.txt','r') as file_read:
        lines = file_read.readlines()
        for each in lines:
            line = each.rstrip()
            cert = "openssl x509 -in {0} -noout -enddate".format(line)
            cert_check = os.popen(cert).read()
            today = time.time()
            print(str(today)+" Expire status cert_path = "+line+" : "+cert_check +'\n')

except:
    print(line + "exceptions occured while reading the cert")


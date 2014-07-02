##################################################################
# dnsmisconfigChkr.py                                                  #
# description: checks if the domain has a dns misconfiguration   #
# author: @shipcod3                                              #
# reference: http://www.securityfocus.com/archive/1/486606       #
##################################################################

import sys, socket, time

print "[**] Checking localhost."+sys.argv[1]+" for DNS Misconfiguration......"
    
#resolve the host

print "[+]Resolving the host address"
try:
    ip_addr = socket.gethostbyaddr("localhost."+sys.argv[1])
    if ip_addr[0] == "localhost":
        print('  >> Vulnerable to DNS Misconfiguration which leads to Same-Site Scripting')
    except socket.error:
        print('  >> Not Vulnerable')   
    
print "[==] Done checking for DNS Misconfiguration"
time.sleep(3)

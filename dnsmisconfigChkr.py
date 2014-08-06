##################################################################
# dnsmisconfigChkr.py                                            #
# description: checks if the domain has a dns misconfiguration   #
# author: @shipcod3                                              #
# reference: http://www.securityfocus.com/archive/1/486606       #
##################################################################

import sys, socket, time

print "********************"
print "* dnsmisconfigChkr *"
print "* by: @shipcod3    *"
print "********************\n"

def usage():
     print("USAGE: python dnsmisconfigChkr.py host.com")  

def dnsmisconfig(argv):
    if len(argv) < 2:
        return usage()
    
    target = sys.argv[1]
    print "[**] Checking localhost."+target+" for DNS Misconfiguration......"
    print "[+]Resolving the host address"
    try:
        ip_addr = socket.gethostbyaddr("localhost."+target)
        if ip_addr[0] == "localhost":
            print('  >> Vulnerable to DNS Misconfiguration which leads to Same-Site Scripting')
    except socket.error:
        print('  >> Not Vulnerable')   
    time.sleep(3)    
    print "[==] Done checking for DNS Misconfiguration"

if __name__ == "__main__":
    dnsmisconfig(sys.argv)

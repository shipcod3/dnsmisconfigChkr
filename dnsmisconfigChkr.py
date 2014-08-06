##################################################################
# dnsmisconfigChkr.py                                            #
# description: checks if the domain has a dns misconfiguration   #
# author: @shipcod3                                              #
# reference: http://www.securityfocus.com/archive/1/486606       #
##################################################################

import sys, socket, time

print """
     _               _                  __ _       ___ _    _       
  __| |_ _  ____ __ (_)___ __ ___ _ _  / _(_)__ _ / __| |_ | |___ _ 
 / _` | ' \(_-< '  \| (_-</ _/ _ \ ' \|  _| / _` | (__| ' \| / / '_|
 \__,_|_||_/__/_|_|_|_/__/\__\___/_||_|_| |_\__, |\___|_||_|_\_\_|  
  by: @shipcod3                              |___/                     
"""
def usage():
     print("USAGE: python dnsmisconfigChkr.py host.com")  

def dnsmisconfig(argv):
    if len(argv) < 2:
        return usage()
    
    target = sys.argv[1]
    payloads = ['localhost', 'dev', 'dns']
    
    for payload in payloads:
        print "[**] Checking "+payload+"."+target+" for DNS Misconfiguration......"
        try:
            print "[+]Resolving the host address " 
            ip_addr = socket.gethostbyaddr(payload+"."+target)
            print ip_addr[2]
            if ip_addr[0] == "localhost":
                print "  >> Vulnerable to DNS Misconfiguration which leads to Same-Site Scripting"
            else:
                print "  >> Not Vulnerable"
        except socket.error:
            print "  >>Host must be down!!"
            print "  >> Not Vulnerable"
    time.sleep(3)    
    print "[==] Done checking for DNS Misconfiguration"

if __name__ == "__main__":
    dnsmisconfig(sys.argv)

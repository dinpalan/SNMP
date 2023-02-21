#! /usr/bin/env python3
#SHEBANG
import os
#import modules with methods in this space

def network():
    print("SNMP v1")
    print("Contact:");os.system(r'snmpget -v1 -c public 198.51.100.1 .1.3.6.1.2.1.1.4.0 | cut -b 32-48');
    print("Name:");os.system(r'snmpget -v1 -c public 198.51.100.1 .1.3.6.1.2.1.1.5.0 | cut -b 32-35')
    print("Location:");os.system(r'snmpget -v1 -c public 198.51.100.1 .1.3.6.1.2.1.1.6.0 | cut -b 32-38')
    print("Number:");os.system(r'snmpget -v1 -c public 198.51.100.1 .1.3.6.1.2.1.2.1.0 | cut -b 32-33')
    print("Uptime:");os.system(r'snmpget -v1 -c public 198.51.100.1 .1.3.6.1.2.1.1.3.0 | cut -b 43-55')
    print("SNMP v2")
    print("Contact:");os.system(r'snmpget -v2c -c public 198.51.100.3 .1.3.6.1.2.1.1.4.0 | cut -b 32-38');
    print("Name:");os.system(r'snmpget -v2c -c public 198.51.100.3 .1.3.6.1.2.1.1.5.0 | cut -b 32-37')
    print("Location:");os.system(r'snmpget -v2c -c public 198.51.100.3 .1.3.6.1.2.1.1.6.0 | cut -b 32-40')
    print("Number:");os.system(r'snmpget -v2c -c public 198.51.100.3 .1.3.6.1.2.1.2.1.0 | cut -b 32-33')
    print("Uptime:");os.system(r'snmpget -v2c -c public 198.51.100.3 .1.3.6.1.2.1.1.3.0 | cut -b 43-55')
    print("SNMP v3")
    print("Contact:");os.system(r'snmpget -v3 -u dinesh -l AuthPriv -a md5 -A cisco123 -x aes -X cisco123 198.51.100.4 .1.3.6.1.2.1.1.4.0 | cut -b 32-40');
    print("Name:");os.system(r'snmpget -v3 -u dinesh -l AuthPriv -a md5 -A cisco123 -x aes -X cisco123 198.51.100.4 .1.3.6.1.2.1.1.5.0 | cut -b 32-36')
    print("Location:");os.system(r'snmpget -v3 -u dinesh -l AuthPriv -a md5 -A cisco123 -x aes -X cisco123 198.51.100.4 .1.3.6.1.2.1.1.6.0 | cut -b 32-37')
    print("Number:");os.system(r'snmpget -v3 -u dinesh -l AuthPriv -a md5 -A cisco123 -x aes -X cisco123 198.51.100.4 .1.3.6.1.2.1.2.1.0 | cut -b 32-33')
    print("Uptime:");os.system(r'snmpget -v3 -u dinesh -l AuthPriv -a md5 -A cisco123 -x aes -X cisco123 198.51.100.4 .1.3.6.1.2.1.1.3.0 | cut -b 43-55')
        
def main():
#write your main function here
       try:
              network()
       except KeyboardInterrupt:
              print("Exiting because of program interpreted by user"); print("Thanks for using my application");

if __name__=='__main__':
       main()


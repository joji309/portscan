import socket
import termcolor


def scan_port(targets, port):
        print('\n' + 'Starting scan For '+ str(target))
        for port in range(1,ports):
        scan_port(target , port)

    try:
        sock =socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened" + str(port))
        sock.close()

    except:
         pass


target = input("[*] Enter Targets to Scan(split them by ,): ")
ports = int(input ("[*] Enter How Many Ports You Want To Scan "))
if ',' in targets:
        print(termcolor.colored(("[+] Scanning Multiple Targets") ,  'green'))
        for ip_addr in targets.split(','):
                scan(ip_addr.strip(' '), ports)

else:
  
    scan(target,ports)                

import subprocess
import os
def isRoot():
    print(os.getuid())
    if(os.getuid()==0):
        return True;
    else:
        return False;
def installFirewalld():
    os.system("yum install firewalld -y")
def makeFirewallSettings():
    os.system("systemctl mask iptables")
    os.system("systemctl enable firewalld")
    os.system("systemctl start firewalld")
def isFirewalldInstalled():
    try:
        true=0
        cmd="./rpm_firewall.sh"
        output=subprocess.check_output(cmd,shell=True)
        for line in output.decode("utf-8").split('\n'):
            if(line.__contains__('firewalld')):
                true=true+1
        if(true>=2):
            return True
        else:
            return False
    except:
        pass
def sshPort():
    f = open("/etc/ssh/sshd_config")
    for line in f.readlines():
        if(line.__contains__("Port") and not line.__contains__("Gateway")):
            if(line[0] == "#"):
                return 22
            else:
                return int (line.split(" ") [1])
def addBlockedIpToFirewall(blockedIp):
    os.system("./firewall.sh "+blockedIp+" "+sshPort())




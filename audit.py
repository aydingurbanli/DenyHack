import subprocess
import os
import time
import Database
def isAuditdInstalled():
    try:
        true=0
        cmd="./rpm_audit.sh"
        output=subprocess.check_output(cmd,shell=True)
        for line in output.decode("utf-8").split('\n'):
            if(line.__contains__('audit')):
                true=true+1
        if(true>=2):
            return True
        else:
            return False
    except:
        pass
def installAuditd():
    os.system("yum install audit audit-libs -y")
def isPathExists():
    try:
        return os.path.exists("/etc/audit/auditd.conf")
    except:
        pass
def notFoundDir():
    try:
        while True:
            inp=input("Can not find auditd config file. Do you want reinstall auditd ? [y/n] : ")
            if(len(inp)>0):
                if(inp[0]=="y"):
                    os.system("yum remeove audit audit-libs -y")
                    os.system("yum install audit audit-libs -y")
                    break
                else:
                    print("Quitting...")
                    time.sleep(3)
                    break
    except:
        pass
def findLogFile():
    try:
        f=open("/etc/audit/auditd.conf")
        for line in f.readlines():
            if(line.__contains__("log_file") and not line.__contains__("max")):
                for splitted in line.split("="):
                    if(splitted.__contains__(".log")):
                        splitted=splitted.rstrip('\n')
                        return splitted.lstrip(" ")
    except Exception as e:
        print(e)
def listFailedAddresses(logFile):
    try:
        ipAddresses=list()
        f=open(logFile)
        for line in f.readlines():
            if(line.__contains__("failed") and line.__contains__("terminal=ssh") and line.__contains__("USER_ERR")):
                for splitted in line.split(" "):
                    if(splitted.__contains__("addr")):
                        for ip in splitted.split("="):
                            if(not ip.__contains__("addr")):
                                ipAddresses.append(ip)

        return ipAddresses
    except Exception as e:
        print(e)

def countFailedAddress(ip,ipAddresses):
    try:
        count=0
        for address in ipAddresses:
            if(address.__eq__(ip)):
                count=count+1
        return count
    except Exception as e:
        print(e)
def makeNonRepeatedList(repeatedList):
    try:
        nonRepeatedList = list ()
        repeatedList.sort()
        for ip in repeatedList:
            if(nonRepeatedList.__contains__(ip)):
                continue
            else:
                nonRepeatedList.append(ip)
        return nonRepeatedList
    except Exception as e:
        print(e)


def addBlockedIpAddressToDatabase(ip):
    try:
        dbase = Database.db ()
        dbase.addRecord(dbase.lastID()+1,ip,countFailedAddress(ip,listFailedAddresses("/var/log/audit/audit.log")))
        dbase.close()
    except TypeError:
        dbase.addRecord(1, ip, countFailedAddress(ip, listFailedAddresses("/var/log/audit/audit.log")))



#for ip in makeNonRepeatedList(listFailedAddresses(findLogFile())):
  #  if (countFailedAddress(ip, listFailedAddresses(findLogFile())) > 2):
 #      addBlockedIpAddressToDatabase(ip)
#addBlockedIpAddressToDatabase("185.147.23.23")



#print(findLogFile())
#analyzeIp("/var/log/audit/audit.log")

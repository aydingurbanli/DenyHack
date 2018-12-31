#!/usr/bin/python3.6
import os,Database,audit,system
def check():
    if(system.isRoot()):
        if(not audit.isAuditdInstalled()):
            audit.installAuditd()
        if(not audit.isPathExists()):
            audit.notFoundDir()
        if(audit.isPathExists()):
            if(not system.isFirewalldInstalled()):
                system.installFirewalld()
            system.makeFirewallSettings()
    else:
        print("DenyHack requires root privileges")
def perform():
    logFile = audit.findLogFile()
    failedAddresses = audit.listFailedAddresses(logFile)
    for ip in audit.makeNonRepeatedList(failedAddresses):
        if(audit.countFailedAddress(ip,failedAddresses) > 2):
            audit.addBlockedIpAddressToDatabase(ip)
            #system.addBlockedIpToFirewall(ip)

db=Database.db()
check()
db.createTable()
perform()
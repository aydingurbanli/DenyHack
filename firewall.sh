#!/usr/bin/env bash
firewall-cmd --direct --permanent --add-rule ipv4 filter INPUT 1 -m tcp --source $1 -p tcp --dport $2 -j REJECT
firewall-cmd --reload
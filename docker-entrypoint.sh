#!/bin/bash

# Update suricata rules
suricata-update

# Start cron
cron

# Add cronjob
crontab /etc/cron.d/suricata-update-cron

# Started suricata
#/usr/bin/suricata -D -c /etc/suricata/suricata.yaml --unix-socket=/pcap/suricata.socket # -i eth0

#python3 /tmp/docker-entrypoint.py

/usr/bin/suricata -c /etc/suricata/suricata.yaml --unix-socket=/socket/suricata.socket # -i eth0
#!/bin/bash

# Update suricata rules
suricata-update

# Start cron
cron

# Add cronjob
crontab /etc/cron.d/suricata-update-cron

# Permissions for bind-mounts
mkdir -p /pcaps
mkdir -p /reports
mkdir -p /socket
#chown appuser:appuser /pcaps
#chown appuser:appuser /reports
#chown appuser:appuser /socket



python /tmp/docker-entrypoint.py &

# Start suricata


while true; do
    /usr/bin/suricata -c /etc/suricata/suricata.yaml --unix-socket=/socket/suricata.socket
    sleep 2000
done



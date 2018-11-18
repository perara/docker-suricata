FROM ubuntu:bionic

RUN apt-get update
RUN apt-get install -y software-properties-common tcpreplay
RUN add-apt-repository -y ppa:oisf/suricata-stable
RUN apt-get install -y suricata
RUN apt-get install -y python3-pip python3-yaml
RUN pip3 install --pre --upgrade suricata-update

# Install cronjob for updating suricata
COPY suricata-update.sh /etc/suricata/suricata-update.sh
COPY suricata-update-cron /etc/cron.d/suricata-update-cron

# Set permissions on cronjob
RUN chmod +x /etc/cron.d/suricata-update-cron

# Copy over entry point
COPY docker-entrypoint.py /tmp/docker-entrypoint.py
RUN chmod +x /tmp/docker-entrypoint.py

COPY docker-entrypoint.sh /tmp/docker-entrypoint.sh
RUN chmod +x /tmp/docker-entrypoint.sh

# Copy suricata configuration
COPY suricata.yaml /etc/suricata/suricata.yaml


ENTRYPOINT ["/tmp/docker-entrypoint.sh"]

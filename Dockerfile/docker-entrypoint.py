import time
import os
import glob
import subprocess
import shutil
import json

if __name__ == "__main__":
    EVE_LOG = "/var/log/suricata/eve.json"

    os.makedirs("/pcap", exist_ok=True)
    os.makedirs("/pcap/completed", exist_ok=True)

    while True:

        for file in glob.glob("/pcap/*.pca*"):

            filename = os.path.basename(file)

            # Clear Eve LOG
            with open(EVE_LOG, "w+") as f:
                f.write("")

            # Run TCP Replay
            subprocess.call(['/usr/bin/tcpreplay', '--topspeed', '--intf1=eth0', file])

            with open(EVE_LOG, "rb") as f:
                alarms = f.read()

            with open("/pcap/completed/" + filename + ".json", "wb") as f:
                f.write(alarms)

            shutil.move(file, "/pcap/completed")

        time.sleep(1)

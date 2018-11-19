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
            open(EVE_LOG, "w").close()

            # Run TCP Replay
            subprocess.call(['/usr/bin/tcpreplay', '--topspeed', '--intf1=eth0', file])

            # Wait a bit
            time.sleep(2)

            #json.load(open(EVE_LOG, "r"))
            print("DONE!")

            shutil.move(file, "/pcap/completed")

        time.sleep(1)



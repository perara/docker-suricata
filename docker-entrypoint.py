import time
import os
if __name__ == "__main__":

    def recursive_permission(p):
        for root, dirs, files in os.walk(p):
            for d in dirs:
                os.chmod(os.path.join(root, d), 0o777)
            for f in files:
                os.chmod(os.path.join(root, f), 0o777)

    fixed = False
    while fixed:

        files = [x for x in os.listdir("/socket")]
        for f in files:
            if ".socket" in f:
                os.chmod(os.path.join("/socket",  f), 0o777)
                fixed = True
        time.sleep(.1)
        """try:
            recursive_permission("/socket")
            recursive_permission("/reports")
            recursive_permission("/pcaps")
            time.sleep(.5)
        except:
            pass"""



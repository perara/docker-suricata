import time
import os
if __name__ == "__main__":

    def recursive_permission(p):
        for root, dirs, files in os.walk(p):
            for d in dirs:
                os.chmod(os.path.join(root, d), 0o777)
            for f in files:
                os.chmod(os.path.join(root, f), 0o777)

    while True:
        recursive_permission("/socket")
        recursive_permission("/reports")
        recursive_permission("/pcaps")
        time.sleep(2)



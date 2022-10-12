import numpy as np
import time

EXEC_TIME = 5
FREQ = 200
DT = 1/FREQ

if __name__ == "__main__":
    start = time.time()

    # Print "ROB311 @UM-ROBOTICS" for 5 seconds @200Hz
    goal = 0
    count = 0
    while(time.time() - start < EXEC_TIME):
        print("ROB311 @UM-ROBOTICS")
        count += 1

        goal += DT
        while((time.time() - start < goal) & (time.time() - start < EXEC_TIME)):
            pass
    t = time.time()
    print("Execution time: " + str(t - start))
    print("Frequency: " + str(count/(t - start)))
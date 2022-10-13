from pickle import TUPLE2
import numpy as np
import time

EXEC_TIME = 5
FREQ = 200
DT = 1/FREQ
RK = 0.11925
RW = 0.04778
ALPHA = np.deg2rad(45)
BETA = np.deg2rad(90)

def compute_motor_torques(Tx, Ty, alpha):
    '''
    Parameters:
    ----------
    Tx: Torque along x-axis
    Ty: Torque along y-axis
    alpha: Motor inclination angle

    Returns:
    --------
            Ty
            T1
            |
            |
            |
            . _ _ _ _ Tx
           / \
          /   \
         /     \
        /       \
       T2       T3

    T1: Motor Torque 1
    T2: Motor Torque 2
    T3: Motor Torque 3

    '''
    Tz = 0

    Fx = Ty/RW
    Fy = Tx/RW

    T1 = 1/3*(Tz + 2/np.cos(alpha)*(Tx*np.cos(BETA)-Ty*np.sin(BETA)))
    T2 = 1/3*(Tz + 1/np.cos(alpha)*(np.sin(BETA)*(-np.sqrt(3)*Tx+Ty)-np.cos(BETA)*( Tx+np.sqrt(3)*Ty)))
    T3 = 1/3*(Tz + 1/np.cos(alpha)*(np.sin(BETA)*( np.sqrt(3)*Tx+Ty)+np.cos(BETA)*(-Tx+np.sqrt(3)*Ty)))

    return T1, T2, T3

if __name__ == "__main__":
    start = time.time()

    T1_array = []
    T2_array = []
    T3_array = []

    goal = time.time()

    while(time.time() - start < EXEC_TIME):
        # Runs @200Hz
        t = time.time()
        Tx = 3.0 * np.sin(t)
        Ty = 2.0 * np.cos(t)

        # Compute Motor Torques
        T1, T2, T3 = compute_motor_torques(Tx, Ty, ALPHA)

        # Append your computed motor torques to their corresponding arrays
        T1_array.append(T1)
        T2_array.append(T2)
        T3_array.append(T3)

        goal += DT
        while((time.time() < goal) & (time.time() - start < EXEC_TIME)):
            pass
    
    # Save your arrays as a .csv file
    T1_array = np.asarray(T1_array)
    T2_array = np.asarray(T2_array)
    T3_array = np.asarray(T3_array)
    data = [T1_array.T, T2_array.T, T3_array.T]
    np.savetxt("data.csv", data, delimiter = ",")
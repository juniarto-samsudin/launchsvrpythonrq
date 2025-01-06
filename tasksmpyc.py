import subprocess
import os
import time
import docker
#from mpyc.runtime import mpc
from mpyc.runtime import setup2 
def launch_server(pid):
    """
    Launch a server on the given IP and port.
    """
    print(f"Launching server on {pid}")

    mpc = setup2(pid)


    async def main():
        print(mpc.parties)
        await mpc.start()
        secint = mpc.SecInt(32)
        if mpc.pid == 0:
            local_table = [[1,2],
                           [3,4]]
            secret_table = [[mpc.input(secint(value)) for value in row] for row in local_table]
        elif mpc.pid == 1:
            local_table = [[5,6],
                          [7,8]]
            secret_table = [[mpc.input(secint(value)) for value in row] for row in local_table]
        elif mpc.pid == 2:
            local_table = [[9,10],
                           [11,12]]
            secret_table = [[mpc.input(secint(value)) for value in row] for row in local_table]   
        await mpc.shutdown()

    mpc.run(main())
    time.sleep(60)
import subprocess
import os
import time

def launch_server(ip, port):
    """
    Launch a server on the given IP and port.
    """
    print(f"Launching server on {ip}:{port}")
    # Example: Launching a Flask app as a subprocess
    subprocess.Popen(
        [
            "python", 
            "server.py", 
            "--host", ip, 
            "--port", str(port)
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        start_new_session=True,
    )
    print(f"Server launched on {ip}:{port}")
    time.sleep(60)
import subprocess
import os
import time
import docker

def launch_server(ip, port):
    """
    Launch a server on the given IP and port.
    """
    print(f"Launching server on {ip}:{port}")
    client = docker.from_env()
    containers = client.containers.list()
    for container in containers:
        print(container.name)
    with open("/etc/hostname", "r") as f:
        container_id = f.read().strip()
    print(f"Container ID: {container_id}")

    container = client.containers.get(container_id)
    port_mappings = container.attrs['NetworkSettings']['Ports']
    print("Port mappings: {} ".format(port_mappings))


    internal_port = '5000/tcp'
    if internal_port in port_mappings and port_mappings[internal_port]:
        print (port_mappings[internal_port][0]["HostPort"])



    # Example: Launching a Flask app as a subprocess
    """ subprocess.Popen(
        [
            "python", 
            "server.py", 
            "--host", ip, 
            "--port", str(port)
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        start_new_session=True,
    ) """
    print(f"Server launched on {ip}:{port}")
    time.sleep(60)
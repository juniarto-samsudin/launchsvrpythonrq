import docker
client = docker.from_env()
containers = client.containers.list()
for container in containers:
    print(container.name)

container = client.containers.get('c428564286a8')
port_mappings = container.attrs['NetworkSettings']['Ports']
print(port_mappings)
#{'5000/tcp': [{'HostIp': '0.0.0.0', 'HostPort': '7001'}, {'HostIp': '::', 'HostPort': '7001'}]}

internal_port = '5000/tcp'
if internal_port in port_mappings and port_mappings[internal_port]:
        print (port_mappings[internal_port][0]["HostPort"])
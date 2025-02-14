from redis import Redis
from rq import Queue
#from tasks import launch_server
from tasks3 import launch_server #RUN A FLASK SERVER IN ONE OF THE WORKER CONTAINERS
#from tasksmpyc import launch_server
import time

# Redis connection
redis_conn = Redis(host="127.0.0.1", port=6379, db=0)
queue = Queue("default", connection=redis_conn)

# Enqueue the server launch task
ip = "0.0.0.0"  # Replace with desired IP
port = 5000       # Replace with desired port
queue.enqueue(launch_server, ip, port)
#queue.enqueue(launch_server, 0)
#time.sleep(2)
#queue.enqueue(launch_server, 1)
#time.sleep(2)
#queue.enqueue(launch_server, 2)

print(f"Enqueued task to launch server on {ip}:{port}")

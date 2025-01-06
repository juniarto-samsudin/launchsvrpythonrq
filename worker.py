from redis import Redis
from rq import Worker, Queue

# Redis connection
redis_conn = Redis(host="redis", port=6379, db=0)
#redis_conn = Redis(host="localhost", port=6379, db=0)
queue = Queue("default", connection=redis_conn)

if __name__ == "__main__":
    worker = Worker([queue])
    worker.work()

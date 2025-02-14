# INSTRUCTIONS 

Multihost Docker means we are using three hosts ["juniarto", "renuga", "neeson].
Each of the host will have to executes the following instructions below.

### On Each Host
1. Deploy all necessary dockers: 

    __*docker compose -f docker-compose3.yml up -d*__

    this will launch redis docker instance (mpc-redisjson) and worker (mpc-worker1)

2. run the following command: 
   
   __*python enqueue.task*__
3. check log for result:

   __*docker logs mpc-worker-1*__

## Note for mpyc package installation

We use __*mpyc-custom = "==0.10.10"*__  in the Pipfile

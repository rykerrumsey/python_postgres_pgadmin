Docker-Compose - Python / Postgres / Pgadmin
==============
1. Make sure you have docker and docker-compose installed on your system.Follow this [link](https://docs.docker.com/compose/install/) for those instructions.

2. Clone this repo to your local computer.

3. Run `docker-compose up` in the top-level directory to start the processes

## After successful launch
* you can access localhost:5000 for the api index route
* you can access localhost:5000/users to get all users from db
* you can access localhost:5001 to connect to pgadmin

NOTE: the password for postgres is in the postgres.env file
NOTE: the login and pass for pgadmin is in the pgadmin.env file

# sqlalchemy-hello-world
Here is an example of a tool with SQL alchemy. This project covered the following aspects:
* Creating and removing docker containers with Postgres.

## How to up a docker container with Postgres.
To build and start a container with Postgres need to execute the following command:
```
docker-compose up -d
```

## How to execute the SQL query manually.
1. Get container ID: 
```
docker ps
```
2. Get POSTGRES_USER from docker-compose.yml.
3. Execute the following command:
```
docker exec -it <CONTAINER_ID> psql -U <POSTGRES_USER>
```

## How to down docker containers.
To stops containers need to execute the following command:
```
docker-compose stop
```
If need to stop and remove containers, need to run the following command:
```
docker-compose down -v
```

## How to prepare all the needed modules.
To install all required modules need to execute:
```
pip install -r requirements.txt
```

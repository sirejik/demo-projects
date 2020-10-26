# elasticsearch-hello-world
Here is an example of a tool with Elasticsearch. This project covered the following aspects:
* Creating and removing docker containers with Elasticsearch and Kibana.

## How to up a docker container with Elasticsearch and Kibana.
To build and start a container with Elasticsearch and Kibana need to execute the following command:
```
docker-compose up
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

## How to run the script.
1. Create config.ini file by example sample_config.ini and specify access to the Elasticsearch.
2. Execute the following command:
```
python main.py
```

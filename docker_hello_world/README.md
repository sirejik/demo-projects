# docker-hello-world
Here is an example of how to build a docker image with a python project. In general, the workflow will look as follows:
* Building the docker image from a specified docker file.
* Running the docker image from an image.
* Deleting a stopped container.

## How to build the docker image from a specified docker file.
```
docker build -t docker-hello-world .
```
## How to run the docker image from an image.
```
docker run -it docker-hello-world
```
## How to list all the running and exited container.
```
docker ps -a
```
## How to delete a stopped container.
```
docker rm <container-name>
```
## How to lists all the locally stored docker images.
```
docker images
```
## How to delete an image from local storage.
```
docker rmi <image-id>
```

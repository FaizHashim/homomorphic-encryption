# Assignment 4

In this assignment, we implement a model that is equivalent to the one described in Assignment 1, except that the cloud server is implemented in a separate container, in order to simulate the fact that the different components may not exist in the same computer. This assignment introduces the basics of Docker and the ideas of containers and images.

## Running the Cloud Server File

The cloud server makes use of binded volumes to store the query data (the number that is to be factorised), and named volumes to store the factors of the query data. First, we need to create the named volume, using the below command. 
**Note:** It is not necessary to create this volume if the named volume already exists.

```
docker volume create factors-db
```

Next, we create an image for the cloud server. This is done by running the Dockerfile present. We perform the following operations inside the directory containing the files.

```
docker docker build -t cloud_server .
```

Finally, we can run the cloud server by creating a container that runs the Python file, `cs.py`. 

```
docker run -dp 127.0.0.1:3000:3000 --mount type=volume,src=factors-db,target=/app/factors_data/ --mount type=bind,src=/temp/data,target=/app/query_data cloud_server
```

This command creates a container, and mounts both the volumes (the named volume and the binded volume) to it. Now, we can move on to running the data owner file and the query user file.

## Running the Data Owner File

In order to run the data owner file, `do.py`, simply run the command,
```
python3 do.py
```

## Running the Query User File

In order to run the query user file, `qu.py`, simply run the command,
```
python3 qu.py
```
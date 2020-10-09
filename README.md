# Simple HTTP Service

A simple _Hello World_ web application.
In the background it utilizes Python3 and Flask.

The web server starts at port 5000 and exposes a HTML page under _/_.

## Building the image

- Check out the code from the git repository and run.

```sh
docker build -t flask-hello-world .
```

- Listing the available images

```sh
docker images
REPOSITORY                                                                  TAG                                                                IMAGE ID            CREATED             SIZE
flask-hello-world                                                           latest                                                             c1440e991356        14 seconds ago      113MB
```

- Start a container and bind the container port 5000.

```sh
docker run -d -p 5000:5000 flask-hello-world:latest
0c362cfed041d0580386e0b7ef24c18317a378a8319744d38f8b81ddf82d3c02
```

## Links

- [Python.org](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

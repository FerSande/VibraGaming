## Vibra Challenge API
Api for search in a csv with queryparameters


## Set Up

For the correct operation of the project it's need to install docker
- [Docker](https://docs.docker.com/get-docker/) - Container platform



## Run the project
- run this command to build the container:
docker build -t "vibrachallenge:Dockerfile" .
- run this command to run the container: 
docker run -d -p 8095:8095 vibrachallenge:Dockerfile 

## Example of request
http://localhost:8095/search?city=Pingshan&quantity=2


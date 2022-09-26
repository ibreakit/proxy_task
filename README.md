# Python Programming Task

## Prerequisites
1. Ensure Docker is installed
2. Set the JWT secret environment variable. This needs to be set in the `Dockerfile` and `docker-compose.yml` by replacing the 'YOUR-KEY-HERE' with your private key value.

## Running the proxy
- For development, you can run `docker-compose up`
- To use make, run `make build` then `make run`. The default port is 8080 but you can change this by passing in a HTTP_PORT variable (e.g `make run HTTP_PORT=9001`)
- To clean the python cache, run `make clean`

## How does it work?
The proxy currently has 3 available routes.

1. GET /
This should return an 'alive' message

2. POST /
This will make a request to an upstream destination, and include an `x-my-jwt` header with the parameters assigned in the task. Providing the upstream request is successful, you should see a message back from the endpoint relaying the JWT value.

3. GET /status
This will return the server uptime. TO DO: Add the number of requests to this endpoint


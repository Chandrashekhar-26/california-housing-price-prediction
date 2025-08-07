## Build Docker Image
#docker build -t california-housing-price-prediction .

# sh
# docker run -it california-housing-price-prediction /bin/sh

## Run
#docker run -d -p 5001:5001 california-housing-price-prediction
#

# Build and Run Docker along with Prometheus
docker-compose up --build

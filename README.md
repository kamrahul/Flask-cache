# Flask-cache Application




# Start service
### docker-compose up -d --build

# Run unit test
### python -m unittest  ( Already added as a step in docker file)


# API Cache Architechture Diagram

![Architechture Image](./images/FlaskCaching.drawio.png)

## First direct request 
### Response time is high
![Without cache](./images/slow_response.JPG)

## Cached request
### Response time is reduced to higher extend
![With cache implementation](./images/fast.JPG)


## In Memory records for request cache
![Redis cache](./images/RedisStore.JPG)
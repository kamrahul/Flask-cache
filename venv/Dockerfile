FROM python:3.7

# Run commands from /app directory inside the docker container
WORKDIR /app

# Copy requirements to /app
COPY requirements.txt /app

#intstall all dependecies for the flask application 
RUN pip3 install -r requirements.txt --no-cache-directory

# Copy all the files from this dir to image
COPY . .

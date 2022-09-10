FROM python:3.10.5

# make sure we have a folder called /app
RUN mkdir /app
# cd into our app folder each time we start up
WORKDIR /app
# copy everything in the project folder into the /app/ folder in docker container
COPY . /app/

RUN pip install -r /app/requirements.txt
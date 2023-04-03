
#  FROM takes a Linux base image and installs python 3.9 on top of that  
FROM python:3.9    

# COPY creates a new folder app and puts all files in that folder within that base image
COPY . /app               
WORKDIR /app
RUN pip install -r requirements.txt

# we need a access a port of the container which has our web application , $ PORT allows the cloud to automatically assign a port 
EXPOSE $PORT         

CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app  

#gunicorn helps to run the python app in the heroku cloud
# workers is used to divide requests , so if we have 1000 requests, 250 requests will be satisfied by each worker
# 0.0.0.0 is the local address in the heroku cloud with port PORT ( which we set  in the last step )
# ie we bind the local ip address in heroku to the port number of the container which is assigned by heroku.
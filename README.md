# About
This is a docker container that uses Flask and MongoDB to host a TO-DO list.

# Installation
```

# Go into the 
cd flask-db-docker

# Create a virtual enviroment
python -m venv .venv

# Activate the virtual enviroment
. .venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Run an build the app
docker-compose up --build
```

#### You can then see your running web app on [localhost:5000](http://localhost:5000)
<hr>

#### And if you want to run the container again, use ```docker-compose up```

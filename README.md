# Flask

## Dependencies 

### Packages

Using python virtual environments is advised. Afterwards use pip to install dependencies.

```
pip install -r requiremnets.txt
```

### Environment variables

To successfully run a flask application, ensure that you set the following environment variables.

#### Linux
```
export FLASK_APP=flashcards.py
export FLASK_ENV=development
```

#### Windows
```
set FLASK_APP=flashcards.py
set FLASK_ENV=development
```

## Running the application
Flask development server is useful during application development, but is not recommended for production deployment for scalability reasons.
```
flask run
```

## Deploying the application

### Self-hosted option
The example below describes steps to deploy Flask application using gunicorn as python web server with nginx as reverse proxy on Ubuntu server.
```
# Install required packages
sudo apt install -y python3 python3-pip git nginx gunicorn3

# Clone this repository from Github
git clone https://github.com/closevision/flask.git

# Install required pip packages 
cd flask
pip3 install -r requirements.txt

# Start gunicorn server instance as daemon
gunicorn3 -D flashcards:app

# Backup default nginx site
sudo mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bkp

# Create a new default site with following content, customize as needed
sudo vim /etc/nginx/sites-available/default

  server {
    listen 80;
    server_name example.org;
    access_log /var/log/nginx/example.org;
    
    location /  {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }

# Restart nginx service
sudo service nginx restart
```
Once nginx successfully restarts the Flask application should be accessible be reachable from your browser, assuming you added a valid entry in clients hosts file.
```
http://example.org/
```




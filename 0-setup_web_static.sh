#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo echo "Betty Holberton" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
the_file="/etc/nginx/sites-available/default"
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data7web_static/current/;}' $the_file
sudo service nginx restart

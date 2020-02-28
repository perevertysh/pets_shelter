#!/bin/bash
project_path=`pwd`
sudo ln -s $project_path/nginx/pettyhome.conf /etc/nginx/sites-enabled/
sudo mkdir /var/www/pettyhome

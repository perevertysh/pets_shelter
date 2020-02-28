#!/bin/bash
project_path=`pwd`
sudo mkdir /var/www/pettyhome
sudo ln -s $project_path/nginx/pettyhome.conf /etc/nginx/sites-enabled/

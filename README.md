GATE CONTROLLER
===============

This is a very simple flask webapp for monitoring and controlling an IP camera and
gate controlled by Raspberry Pi GPIO

Install necessary packages
------------------------------------------

    $ apt update
    $ apt upgrade

Install necessary packages

    $ apt install build-essential supervisor

Install Python

    $ apt-get install python2.7-dev python-setuptools

Setup Git
------------------------------------------

Install git

    $ apt-get install git-core

Generate a new SSH key

    $ ssh-keygen -t rsa -C "your_email@youremail.com"

Then add the key from __~/.ssh/id_rsa.pub__ to GitHub as a deployment key

Test the key by

    $ ssh -T git@github.com

Install Virtualenv
------------------------------------------

Install virtualenv

    $ pip install virtualenv
    
Install nginx
------------------------------------------

Install nginx

    $ apt-get install nginx

Install uWSGI
------------------------------------------

Install uWSGI

    $ apt-get install uwsgi uwsgi-plugin-python

Configuration
=========================================

Get source code
-----------------------------------------

    $ cd /var/www
    $ git clone git@github.com:[username]/gate_control.git
    
Set owner to www-data

    $ chown -R www-data:www-data /var/www/gate_control

Setup folder structure
-----------------------------------------

Create folders

    $ cd /web/example.com/
    $ mkdir logs public_html source

Setup virtualenv
-----------------------------------------

    $ cd /var/www
    $ virtualenv gate_control_venv

Install deps

    $ pip install flask, rpi.GPIO

Config nginx
-----------------------------------------

    $ cp ${repo}/resources/nginx/cameras /etc/nginx/sites-available/

Then create a symlink

    $ ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/example.com

Then you may need to delete default site

    $ rm /etc/nginx/sites-enabled/default

Config uwsgi
-----------------------------------------

    $ cp ${repo}/resources/uwsgi/cameras.conf /etc/uwsgi/apps-available/

Then create a symlink

    $ ln -s /etc/uwsgi/apps-available/cameras.conf /etc/uwsgi/apps-enabled/cameras.conf

Config supervisord
-----------------------------------------

    $ cp ${repo}/resources/supervisord/camera_images.conf /etc/supervisor/conf.d/
    $ supervisorctl reread
    $ supervisorctl update

Restart server
=========================================

    $ service uwsgi restart
    $ service nginx restart


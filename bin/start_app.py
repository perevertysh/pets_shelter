import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

username = "user"

if not os.path.islink("/etc/nginx/sites-enabled/pettyhome.conf"):
    os.system("sudo rm /etc/nginx/sites-enabled/default")
    os.system("sudo mkdir /var/www/pettyhome")
    os.system("sudo chown {} /var/www/pettyhome".format(username))
    os.system("sudo ln -s {}/nginx/pettyhome.conf /etc/nginx/sites-enabled/".format(path))
    os.system("sudo service nginx restart")
os.system("source {}/../pettyenv/bin/activate".format(path))
os.system("python manage.py collectstatic")
os.system("exec gunicorn  -c '{}/gunicorn-config.py' pettyhome.wsgi".format(path))

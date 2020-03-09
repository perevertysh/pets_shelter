import os
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

username = env("USERNAME")

if not os.path.islink("/etc/nginx/sites-enabled/pettyhome.conf"):
    os.system("sudo rm /etc/nginx/sites-enabled/default")
    os.system("sudo mkdir /var/www/pettyhome")
    os.system("sudo chown {} /var/www/pettyhome".format(username))
    os.system("sudo ln -s {}/nginx/pettyhome.conf /etc/nginx/sites-enabled/".format(path))
os.system("sudo service nginx restart")
os.system("cd {}/frontend; npm install; npm run production".format(path))
os.system("python manage.py collectstatic --noinput")
os.system("python manage.py migrate")
os.system("exec gunicorn  -c '{}/bin/gunicorn-config.py' pettyhome.wsgi".format(path))


# python manage.py loaddata pets/fixtures/data.json petdocs/fixtures/data.json

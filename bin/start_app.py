import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.system("source {}/../pettyenv/bin/activate".format(path))
os.system("python manage.py collectstatic")
os.system("exec gunicorn  -c '{}/gunicorn-config.py' pettyhome.wsgi".format(path))

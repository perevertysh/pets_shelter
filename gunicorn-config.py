import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


command = '{}/../pettyenv/bin/gunicorn'.format(path)
pythonpath = '{}'.format(path)
bind = '127.0.0.1:8001'
workers = 5
user = 'user'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=pettyhome.settings'
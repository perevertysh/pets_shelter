command = '/home/perevertysh/factory/fta/pettyenv/bin/gunicorn'
pythonpath = '/home/perevertysh/factory/fta/pettyhome'
bind = '127.0.0.1:8001'
workers = 5
user = 'perevertysh'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=pettyhome.settings'
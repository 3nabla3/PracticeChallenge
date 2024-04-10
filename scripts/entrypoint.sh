#! /bin/bash

flag=$(cat ./FLAG)

python3 manage.py migrate
python3 manage.py shell_plus -c "Secret.objects.create(value='$flag')"
python3 manage.py createsuperuser --noinput --username admin --email admin@example.com
python3 manage.py runserver 0.0.0.0:8000

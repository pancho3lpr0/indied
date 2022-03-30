web: gunicorn.wsgi:aplication --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
web: gunicorn indeed_jfpp.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
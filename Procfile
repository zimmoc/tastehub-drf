release: python manage.py makemigrations && python manage.py migrate

web: gunicorn tastehub_drf.wsgi

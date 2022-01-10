web: gunicorn drf.wsgi
release: python3 manage.py makemigration --noinput
release: python3 manage.py collectstatic --noinput
release: python3 manage.py migrate --noinput


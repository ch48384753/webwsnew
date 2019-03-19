

python3 manage.py makemigrations tour
python3 manage.py migrate
python3 manage.py createsuperuser

#get sql
python3 manage.py sqlmigrate tour 0001

#start webserver
python3 manage.py runserver 

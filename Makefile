run:
	@python django_app/manage.py runserver 0.0.0.0:8000
install:
	@pip install -r requirements.txt
	@pip install git+https://github.com/noamsu/django-facebook-connect.git

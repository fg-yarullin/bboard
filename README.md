# Создание виртуальной среды

	mkvirtualenv my_django_environment 

Теперь вы находитесь внутри виртуальной области и можете установить Django и начать разработку.

С этого момента любые команды запускаются в виртуальной среде Python

# Использование виртуальной среды

workon my_django_environment
	
deactivate — Выход из текущей виртуальной среды Python
workon — Список доступных виртуальных сред
workon name_of_environment — Активация конкретной виртуальной среды Python
rmvirtualenv name_of_environment — Удаление конкретной виртуальной среды.

# Установка Django

После создания виртуальной среды и вызова workon для входа в неё вы можете использовать pip3 для установки Django.
	
	pip3 install django

	pip3 install django-bootstrap4
	
	mkdir django_test
	cd django_test
	python3 manage.py runserver

# Running database migrations:

	python3 manage.py makemigrations
	python3 manage.py migrate

# Running the website

	python3 manage.py runserver
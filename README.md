# recipe-app-api
Recipe app api source code

### useful commands

Run after create a new module
> docker-compose run app sh -c "python manage.py test && flake8"

Run the migrations from the models.
> docker-compose run app sh -c "python manage.py makemigrations core"


# Python and MySQL containerized application

## Project objective
The project is a study on how to run a simple application using containers. The app has two components, a Python script and a MySQL database. In order to run the app, we will use two options: first Docker Compose and second Minikube.
In the database_sql folder we have a SQL file with a MySQL database. In the database_manager folder we have a main.py file with a Python script which makes a query to the database.
For part 1 of the study, we want to write a Docker-compose file so that we create a container with the Python script, a container with the MySQL database and the Python script makes a query to the database container.
For part 2 of the study, instead of Docker Compose we want to use Minikube and yaml configuration files to deploy our two apps.

## Instalation and Testing

Steps:

### Database-manager folder
- in the database_manager folder use pipenv for dependency management.
- create requirements.txt file: `pip freeze > requirements.txt`
- create a .env file based on the structure of the config.py file
- in the database_manager folder, config.py file, change the parameter of the `load_dotenv()` function to include the path to of your .env file
- optional, in the logging_production_docker.config file, update the value of the `args` key in the `[handler_rotatingFileHandler]` section

### Database-sql folder
- create dockerfile according to the `dockerfile-model` file present in the folder.

### Main app folder

#### 1. If using Docker Compose:
- if using vs code:
    - open new wsl ubuntu window
- in new terminal, go to the `database_manager` folder and create the Python app image::
    - `docker build -f dockerfile -t image_hardware_app_python .`
- go to the `database_sql` folder and create the MySQL app image::
    - `docker build -f dockerfile -t image_hardware_app_mysql .` 
- Create a `hardware_app.env` file based on the model file found in the directory.
- in docker-compose file folder run:
    `docker-compose up`
- create docker volume:
    `docker volume create hardware-app-volume`

#### 2. For Kubernetes, use Windows WSL2 with Ubuntu22 and Minikube with Docker driver.
- create python service dockerfile and sql service dockerfile in their respective folders
- Create a `mysql-secret.yaml` file based on the `mysql-secret model.yaml` file present in the directory.
- if using vs code:
    - open new wsl ubuntu window
- in new terminal, go to the `database_manager` folder and create the Python app image::
    - `docker build -f dockerfile -t image_hardware_app_python .`
- go to the `database_sql` folder and create the MySQL app image::
    - `docker build -f dockerfile -t image_hardware_app_mysql .` 


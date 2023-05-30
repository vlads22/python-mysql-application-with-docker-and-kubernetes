# Python and MySQL containerized application

## Project objective
Create an example of how to run a simple Python & MySQL application using containers.
The app has two components, a Python script and a MySQL database.
In order to containerize and run the app, we will use two options: first Docker Compose and second Kubernetes with Minikube.
In the database_sql folder we have a SQL file with a MySQL database.
In the database_manager folder we have a main.py file with a Python script which makes a query to the database.
For part 1 of the project, we want to write a Docker-compose file with which we create a container with the Python script, a container with the MySQL database and the Python script makes a query to the database.
For part 2 of the project, instead of Docker Compose we want to use Minikube and yaml configuration files to deploy our two containers.

## Instalation and Testing

Steps:

### Database-manager folder
- In the `database_manager` folder use pipenv for dependency management.
- Create requirements.txt file: `pip freeze > requirements.txt`.
- Create a `.env` file based on the structure of the config.py file.
- In the `config.py` file, change the parameter of the `load_dotenv()` function to include the path to your `.env` file.
- Optional, in the `logging_production_docker.config` file, update the value of the `args` key in the `[handler_rotatingFileHandler]` section.

### Database-sql folder
- Create dockerfile according to the `dockerfile-model` file present in the folder.

### Main folder

#### 1. If using Docker Compose:
- If using VS Code:
    - Open new wsl2 ubuntu window.
- In new terminal, go to the `database_manager` folder and create the Python app image:
    - `docker build -f dockerfile -t image_mov_app_python .`
- Go to the `database_sql` folder and create the MySQL app image:
    - `docker build -f dockerfile -t image_mov_app_mysql .` 
- Create a `movie_app.env` file based on the model file found in the directory.
- In the main folder run:
    `docker-compose up`
- Create docker volume:
    `docker volume create mov-app-volume`

#### 2. For Kubernetes, use Windows WSL2 with Ubuntu22 and Minikube with Docker driver.
- Create the Python service dockerfile and SQL service dockerfile in their respective folders (or use the ready to go yaml file already present in the folder).
- Create a `mysql-secret.yaml` file based on the `mysql-secret model.yaml` file present in the directory.
- If using VS Code:
    - Open new WSL Ubuntu window.
- In new terminal, go to the `database_manager` folder and create the Python app image:
    - `docker build -f dockerfile -t image_mov_app_python .`
- Go to the `database_sql` folder and create the MySQL app image:
    - `docker build -f dockerfile -t image_mov_app_mysql .` 


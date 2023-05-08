from typedconfig import Config, key, section, group_key
from typedconfig.source import EnvironmentConfigSource
import os
import json
from dotenv import load_dotenv


def parse_string(string):
    parsed = json.loads(string)
    return parsed


@section('APP')
class APP(Config):
    LOGGING_CONFIG = key(cast=str)
    # LOGGING_FILE = key(cast=str)


@section('DB_HARDWARE')
class DB_HARDWARE(Config):
    HOST = key(cast=str)
    DATABASE = key(cast=str)
    USER = key(cast=str)
    PASSWORD = key(cast=str)
    PORT = key(cast=int)


class AppConfig(Config):
    APP = group_key(APP)
    DB_HARDWARE = group_key(DB_HARDWARE)


def read_configuration() -> AppConfig:

    # BASEDIR = os.path.abspath(os.path.dirname("C:\configurations\hardware-app\.env"))
    # env_path = os.path.join(BASEDIR, '.env')
    #env_path = "C:\configurations\hardware-app-configuration\dev\database\.env"
    #load_dotenv(env_path)
    
    load_dotenv() # take environment variables from .env.
    config = AppConfig()
    config.add_source(EnvironmentConfigSource())
    config.read()
    return config

# config = read_configuration()
# print(config.DB_HARDWARE.DATABASE)

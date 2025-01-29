from pydantic_settings import BaseSettings

# ANOTHER WAY
# import os
# from dotenv import load_dotenv
# load_dotenv(".env_example")
#
# database_hostname = os.getenv("DATABASE_HOSTNAME")
# database_password = os.getenv("DATABASE_PASSWORD")
# database_username = os.getenv("DATABASE_USERNAME")
# database_port = os.getenv("DATABASE_PORT")
# database_name = os.getenv("DATABASE_NAME")

class Settings(BaseSettings):
    database_hostname: str
    database_password: str
    database_username: str
    database_name: str
    database_port: str
    class Config:
        env_file = ".env_example"

settings = Settings()
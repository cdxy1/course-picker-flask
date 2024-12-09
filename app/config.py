import os


class Config:
    APPNAME = "app"
    ROOT_PATH = os.path.abspath(APPNAME)
    UPLOAD_PATH = "/static/uploads/"
    SERVER_PATH = ROOT_PATH + UPLOAD_PATH

    USER = os.environ.get("POSTGRES_USER")
    PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    HOST = os.environ.get("POSTGRES_HOST")
    PORT = os.environ.get("POSTGRES_PORT")
    DB = os.environ.get("POSTGRES_DB")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = "32423fgerger435greerge43t34"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

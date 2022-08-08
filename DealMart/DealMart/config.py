from . import env

def get_var(var_name, default="throw_error"):
    value_from_env = getattr(env, var_name, default)
    if value_from_env == "throw_error":
        raise Exception(f"Missing value of {var_name} in environment")
    return value_from_env


class Config:
    # Environment Specific Variables
    DEBUG_MODE = get_var("DEBUG", False)
    SECRET_KEY = get_var("SECRET_KEY")
    ENGINE=get_var("ENGINE")
    NAME=get_var("NAME")
    USER=get_var("USER")
    PASSWORD=get_var("PASSWORD")
    HOST=get_var("HOST")
    EMAIL_BACKEND = get_var("EMAIL_BACKEND")
    EMAIL_HOST = get_var("EMAIL_HOST")
    EMAIL_PORT = get_var("EMAIL_PORT")
    EMAIL_USE_TLS = get_var("EMAIL_USE_TLS")
    EMAIL_HOST_USER = get_var("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = get_var("EMAIL_HOST_PASSWORD")

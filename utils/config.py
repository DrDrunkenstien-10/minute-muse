from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_env_variable(var_name, default=None):
    return os.getenv(var_name, default)

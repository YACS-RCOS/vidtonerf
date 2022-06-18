"""
This file loads the environment variables from the .env file.
Afterwards, the Web Server is started.
"""

from config import load_dotenv
from webserver import WebServer

if __name__ == "__main__":
    env_vars = load_dotenv()
    port = 5000 if "PORT" not in env_vars else int(env_vars["PORT"])
    # default to listening on 5000

    WebServer(port=port).run()

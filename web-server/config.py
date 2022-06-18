"""
This file contains the method that loads the
.env environment variables file to be used in the application.
"""

from typing import Dict


def load_dotenv(fp: str = ".env") -> Dict[str, str]:
    env_dict = dict()
    with open(fp, "r") as f:
        for line in f:
            key, val = line.strip().split("=")
            env_dict[key] = val
            # just a side note, all keys and vals are strings

    return env_dict

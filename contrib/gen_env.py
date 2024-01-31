"""
Responsible for speeding up the generation of a local '.env' configuration file.
OBS: Run in development environment only
"""

import os

from django.core.management.utils import get_random_secret_key


def dict_to_config_string(data: dict) -> str:
    config_string = ""
    for key, value in data.items():
        config_string += f"{key}=\"{value}\"\n"

    return config_string.strip()


def generate_env():
    env_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"
    )

    if os.path.exists(env_path):
        print("A .env file already exists, delete it and run again")
        return

    VARIABLES = {
        "DEBUG": True,
        "ALLOWED_HOSTS": "*",
        "SECRET_KEY": get_random_secret_key(),
        "DATABASE_URL": "postgresql://apiphantom:apiphantom@localhost:5432/apiphantom",
    }

    with open(env_path, "w") as configfile:
        configfile.write(dict_to_config_string(VARIABLES))


if __name__ == "__main__":
    generate_env()
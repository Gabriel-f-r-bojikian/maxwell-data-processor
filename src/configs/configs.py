from os.path import dirname, realpath, join
from typing import Optional

from pydantic import BaseSettings


class Configs(BaseSettings):
    LOG_PATH: Optional[str]

    class Config:
        env_file = join(dirname(realpath(__file__)), ".env")
        case_sensitive = True
        env_file = ".env"


configs = Configs()

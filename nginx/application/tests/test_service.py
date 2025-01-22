from nginx.application.helper.plataform import get_nginx
from nginx.domain.config import Config
import pytest

nginx_plataform = get_nginx()

nginx = nginx_plataform(Config(
    path_nginx="",
    path_log="",
    password=""
))



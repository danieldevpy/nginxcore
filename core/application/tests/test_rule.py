from core.application.helper.plataform import get_nginx
from core.domain.config import Config
from core.application.helper.nginx import make_rule, make_embbed_config
import pytest, os

nginx_plataform = get_nginx()

nginx = nginx_plataform(Config(
    path_nginx="/etc/nginx",
    path_log="/var/log/nginx",
    password="devpython"
))

name_rule = "teste"

def test_create_rule():
    path = nginx.config.get_path_avaliable(name_rule)
    assert os.path.exists(path) == False
    nginx.create_rule(name_rule, make_rule(server_name="localhost", proxy_pass="localhost"))
    assert os.path.exists(path) == True
    nginx.delete_rule(name_rule)

def test_delete_rule():
    path = nginx.config.get_path_avaliable(name_rule)
    nginx.create_rule(name_rule, make_rule(server_name="localhost", proxy_pass="localhost"))
    assert os.path.exists(path) == True
    nginx.delete_rule(name_rule)
    assert os.path.exists(path) == False

def test_rule_config():
    config_rule = make_rule(server_name="localhost", proxy_pass="localhost")
    with pytest.raises(Exception):
        nginx.test_rule_configuration(config_rule)
    config = make_embbed_config(config_rule)
    nginx.test_rule_configuration(config)
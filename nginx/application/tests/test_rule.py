from nginx.application.helper.plataform import get_nginx
from nginx.domain.config import Config
from nginx.application.helper.nginx import make_rule, make_embbed_config
import pytest, os
from conftest import path_nginx_mock, path_log_mock, name_rule

nginx_plataform = get_nginx()
nginx = nginx_plataform(Config(
    path_nginx=path_nginx_mock,
    path_log=path_log_mock,
    password="devpython"
))

def test_create_rule():
    path = nginx.config.get_path_avaliable(name_rule)
    assert os.path.exists(path) == False
    nginx.create_rule(name_rule, make_rule(name_rule=name_rule,server_name="localhost", proxy_pass="localhost"))
    assert os.path.exists(path) == True
    nginx.delete_rule(name_rule)

def test_delete_rule():
    path = nginx.config.get_path_avaliable(name_rule)
    nginx.create_rule(name_rule, make_rule(name_rule=name_rule,server_name="localhost", proxy_pass="localhost"))
    assert os.path.exists(path) == True
    nginx.delete_rule(name_rule)
    assert os.path.exists(path) == False

def test_rule_config():
    config_rule = make_rule(name_rule=name_rule,server_name="localhost", proxy_pass="localhost")
    with pytest.raises(Exception):
        nginx.test_rule_configuration(config_rule)
    config = make_embbed_config(config_rule)
    nginx.test_rule_configuration(config)

def test_get_rule_log():
    _make_file_log_(name_rule)
    assert len(nginx.get_rule_log(name_rule)) == 11


def _make_file_log_(name):
    with open(f"{path_log_mock}/{name}_access.log", "wb") as file:
        file.write(f"""127.0.0.1 - - [21/Jan/2025:16:05:09 -0300] "GET /rules HTTP/1.1" 200 2853 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
127.0.0.1 - - [21/Jan/2025:16:05:10 -0300] "GET / HTTP/1.1" 200 1573 "http://localhost/rules" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
127.0.0.1 - - [21/Jan/2025:16:05:11 -0300] "GET / HTTP/1.1" 200 1573 "http://localhost/rules" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
127.0.0.1 - - [21/Jan/2025:16:21:44 -0300] "GET /rules HTTP/1.1" 200 2853 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
127.0.0.1 - - [21/Jan/2025:16:23:00 -0300] "GET /rules HTTP/1.1" 200 2853 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
127.0.0.1 - - [21/Jan/2025:16:23:03 -0300] "GET /rules HTTP/1.1" 200 2853 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
127.0.0.1 - - [21/Jan/2025:16:23:21 -0300] "GET /rules HTTP/1.1" 200 2853 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
127.0.0.1 - - [21/Jan/2025:16:23:27 -0300] "GET /rules HTTP/1.1" 200 2853 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
127.0.0.1 - - [21/Jan/2025:16:23:29 -0300] "GET /rules HTTP/1.1" 200 2853 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
127.0.0.1 - - [21/Jan/2025:16:24:50 -0300] "GET /rules HTTP/1.1" 200 2853 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
""".encode())

import os, shutil

current_path = os.getcwd()
name_rule = "teste"
path_nginx_mock = f"{current_path}/nginx/application/tests/nginx"
_path_nginx_avaliable = f"{current_path}/nginx/application/tests/nginx/sites-available/"
_path_nginx_enabled = f"{current_path}/nginx/application/tests/nginx/sites-enabled/"
path_log_mock = f"{current_path}/nginx/application/tests/log"


def pytest_configure(config):
    os.mkdir(path_nginx_mock)
    os.mkdir(path_log_mock)
    os.mkdir(_path_nginx_avaliable)
    os.mkdir(_path_nginx_enabled)

def pytest_unconfigure(config):
    shutil.rmtree(_path_nginx_avaliable)
    shutil.rmtree(_path_nginx_enabled)
    shutil.rmtree(path_nginx_mock)
    shutil.rmtree(path_log_mock)
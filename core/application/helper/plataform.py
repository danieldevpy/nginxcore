import platform
from core.application.repository.nginx import Nginx
from core.application.controler.linux import NginxLinux
from typing import Type

def get_nginx() -> Type[Nginx]:
    system_name = platform.system()
    if system_name == 'Linux':
        return NginxLinux
    elif system_name == 'Windows':
        return None


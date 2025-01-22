import subprocess
import platform
from nginx.domain.command import Command


class ProcessSystem:

    @classmethod
    def execute(cls, command: Command, password: str):
        # Detectar o sistema operacional
        os_name = platform.system().lower()

        # Se for Linux ou macOS
        if os_name in ['linux', 'darwin']:
            return subprocess.run(
                command.args,
                input=password + '\n',  # No Linux/macOS, geralmente é assim que passamos a senha para 'sudo'
                check=command.check,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

        # Se for Windows
        elif os_name == 'windows':
            # Para Windows, se precisar de elevacao de permissões, pode-se usar o runas
            # Isso pode variar dependendo do que você está tentando fazer
            command_with_runas = ["runas", "/user:Administrator"] + command.args
            return subprocess.run(
                command_with_runas,
                check=command.check,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        else:
            raise Exception(f"Sistema operacional {os_name} não suportado.")


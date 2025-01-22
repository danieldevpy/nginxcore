from nginx.application.repository.nginx import Nginx
from nginx.domain.command import Command
from nginx.application.helper.temp import create_file
from nginx.application.helper.nginx import get_access
import os

class NginxLinux(Nginx):

    def restart(self):
        self._execute_command(Command(
            name="Reiniciar Serviço Nginx",
            args=["sudo", "-S", "systemctl", "restart", "nginx"]
        ))

    def test_rule_configuration(self, config):
        return self._execute_command(Command(
            name="Testar Arquivo de Regra",
            args=['sudo', '-S', 'nginx', '-t', '-c', create_file(config)],
        ))
    
    def get_rules(self):
        return self._execute_command(Command(
            name="Obter Regra de Configuração do Nginx",
            args=["sudo", "-S", "ls", self.config.get_path_avaliable()]
        )).stdout.split('\n')[:-1]

    def get_rule(self, name):
        return self._execute_command(Command(
            name="Obter Regra de Configuração do Nginx",
            args=["sudo", "-S", "cat", self.config.get_path_avaliable(name)]
        )).stdout

    def create_rule(self, name, config):
        self._execute_command(Command(
            name="Mover Arquivo de Configuração para as Regras do Nginx",
            args=["sudo", "-S", "mv", create_file(config), self.config.get_path_avaliable(name)]
        ))

    def delete_rule(self, name):
        self._execute_command(Command(
            name="Deletar Arquivo de Regra",
            args=["sudo", "-S", "rm", "-rf", self.config.get_path_avaliable(name)]
        ))

    def activate_rule(self, name):
        self._execute_command(Command(
            name="Criar Link Simbólico para Ativar Regra no Nginx",
            args=["sudo", "-S", "ln", "-s", self.config.get_path_avaliable(name), self.config.get_path_enabled()]
        ))
    
    def disable_rule(self, name):
        self._execute_command(Command(
            name="Remover Link Simbólico para Desatuvar Regra no Nginx",
            args=["sudo", "-S", "rm", "-f", self.config.get_path_enabled(name)]
        ))

    def check_rule_is_active(self, name):
        return os.path.exists(self.config.get_path_enabled(name))

    def get_rule_log(self, name):
        path = self.config.get_path_log_access(name)
        if not os.path.exists(path):
            raise Exception("Log não encontrado!")
        cat = self._execute_command(Command(
            name="Ler Arquivo de LOG",
            args=["sudo", "-S", "cat", path]
        )).stdout
        accesses = [get_access(line) for line in cat.split("\n")]
        return accesses



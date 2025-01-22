from abc import ABC, abstractmethod
from dataclasses import dataclass
from core.domain.config import Config
from core.application.helper.process import ProcessSystem
from core.domain.command import Command

@dataclass
class Nginx(ABC):
    config: Config

    """
    Base class para interagir com os serviços e configurações do Nginx.
    Define uma interface abstrata que deve ser implementada por subclasses específicas.
    """
    def _execute_command(self, command: Command):
        try:
            return ProcessSystem.execute(
                command=command,
                password=self.config.password
            )
        except Exception as e:
            raise Exception(f"Erro ao executar comando '{command.name}'. Detalhes: {str(e)}") from e

    """FUNCTIONS SERVICE"""
    @abstractmethod
    def restart(self):
        """
        Reinicia o serviço do Nginx.
        
        Deve ser implementado para garantir que o serviço seja reiniciado corretamente
        após alterações na configuração ou manutenção.
        """
        raise NotImplementedError
    
    @abstractmethod
    def test_rule_configuration(self, config: str):
        """
        Testa a validade da configuração do Nginx.

        Deve verificar a sintaxe e validar se as regras configuradas estão corretas
        antes de aplicar alterações. Normalmente utiliza o comando `nginx -t`.
        """
        raise NotImplementedError
    
    """FUNTIONS RULES"""

    @abstractmethod
    def get_rule(self, name: str):
        """
        Recupera uma regra configurada no Nginx.

        Deve buscar uma regra específica com base nos critérios fornecidos,
        como nome, ID ou outro identificador.
        """
        raise NotImplementedError
    
    @abstractmethod
    def create_rule(self, name: str, config: str):
        """
        Cria uma nova regra no Nginx.

        Deve adicionar uma nova configuração, como regras de proxy, bloqueio,
        ou outros ajustes relacionados à segurança ou ao tráfego.
        """
        raise NotImplementedError
    
    @abstractmethod
    def delete_rule(self, name: str):
        """
        Remove uma regra existente do Nginx.

        Deve ser implementado para excluir uma regra específica, garantindo
        que ela não interfira mais na configuração.
        """
        raise NotImplementedError
    
    @abstractmethod
    def activate_rule(self, name: str):
        """
        Ativa uma regra no Nginx.

        Deve implementar o processo de habilitação de uma regra, incluindo
        alterações nos arquivos de configuração e recarregamento do serviço, se necessário.
        """
        raise NotImplementedError

    @abstractmethod
    def disable_rule(self):
        """
        Desativa uma regra no Nginx.

        Deve implementar o processo de desabilitar uma regra sem removê-la completamente,
        permitindo reativá-la posteriormente.
        """
        raise NotImplementedError

    @abstractmethod
    def check_rule_is_active(self):
        """
        Verifica se uma regra específica está ativa no Nginx.

        Deve buscar a configuração atual e determinar se a regra está em vigor.
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_rule_log(self):
        """
        Recupera os logs relacionados a uma regra no Nginx.

        Deve acessar os logs do Nginx (geralmente localizados em `/var/log/nginx/`)
        e filtrar as informações relacionadas a uma regra específica.
        """
        raise NotImplementedError

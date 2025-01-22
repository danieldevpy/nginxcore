from dataclasses import dataclass


@dataclass
class Config:
    path_nginx: str
    path_log: str
    password: str

    def get_path_avaliable(self, rule: str = None) -> str:
        if rule:
            return f"{self.path_nginx}/sites-available/{rule}"
        return f"{self.path_nginx}/sites-available/"

    def get_path_enabled(self, rule: str = None) -> str:
        if rule:
            return f"{self.path_nginx}/sites-enabled/{rule}"
        return f"{self.path_nginx}/sites-enabled/"

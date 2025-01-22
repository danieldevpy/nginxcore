from dataclasses import dataclass

@dataclass
class LogAccess:
    ip: str
    user: str
    date: str
    method: str
    path: str
    http_version: str
    status: str
    size: str
    referer: str
    user_agent: str
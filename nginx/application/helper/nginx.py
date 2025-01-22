import re
from nginx.domain.access import LogAccess

def make_embbed_config(config: str):
    return f'''
        events {{}}
        http {{
            {config}
        }}
    '''

def make_rule(name_rule: str, server_name: str, proxy_pass: str) -> str:
    return f"""server {{
    listen 80;
    server_name {server_name};
    client_max_body_size 5M;
    access_log /var/log/nginx/{name_rule}_access.log;
    error_log /var/log/nginx/{name_rule}_error.log;

    location / {{
        if ($uri != "/IDS/CAP.XML") {{
            proxy_pass http://{proxy_pass};
        }}
    }}
}}
"""

def get_pattern_access():
    return re.compile(
    r'(?P<ip>[\d\.]+) - (?P<user>\S+) \[(?P<date>.+?)\] '
    r'"(?P<method>\S+) (?P<path>\S+) HTTP/(?P<http_version>[\d\.]+)" '
    r'(?P<status>\d+) (?P<size>\d+|-) "(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)"'
    )

def get_access(line: str):
    pattern = get_pattern_access()
    match = pattern.match(line)
    if not match:
        return None
    data = match.groupdict()
    return LogAccess(
        ip=data["ip"],
        user=data["user"] if data["user"] != "-" else None,
        date=data["date"],
        method=data["method"],
        path=data["path"],
        http_version=data["http_version"],
        status=int(data["status"]),
        size=int(data["size"]) if data["size"] != "-" else 0,
        referer=data["referer"],
        user_agent=data["user_agent"]
    )
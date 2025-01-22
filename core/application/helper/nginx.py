
def make_embbed_config(config: str):
    return f'''
        events {{}}
        http {{
            {config}
        }}
    '''

def make_rule(server_name: str, proxy_pass: str) -> str:
    return f"""server {{
    listen 80;
    server_name {server_name};
    client_max_body_size 5M;
    access_log /var/log/nginx/{server_name}_access.log;
    error_log /var/log/nginx/{server_name}_error.log;

    location / {{
        if ($uri != "/IDS/CAP.XML") {{
            proxy_pass http://{proxy_pass};
        }}
    }}
}}
"""

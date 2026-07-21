#!/usr/bin/env python3
"""
PRO-TCHAD-STUD
Plateforme éducative avancée pour comprendre les protocoles réseau en pratique.
Créée par la communauté tchadienne d'apprentissage.

Usage : sudo python pro_tchad_stud.py
"""

import socket
import subprocess
import sys
import time
import urllib.request
from datetime import datetime


# ==== STYLES TERMINAL ====
class Style:
    GREEN = '\033[92m'
    DARK_GREEN = '\033[32m'
    BLACK_BG = '\033[40m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'


def clear():
    subprocess.run("clear" if sys.platform != "win32" else "cls", shell=True)


def typing(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def banner():
    clear()
    print(Style.BLACK_BG + Style.GREEN + Style.BOLD)
    print("""
    ██████╗ ██████╗  ██████╗      ████████╗ ██████╗██╗  ██╗ █████╗ ██████╗ 
    ██╔══██╗██╔══██╗██╔═══██╗     ╚══██╔══╝██╔════╝██║  ██║██╔══██╗██╔══██╗
    ██████╔╝██████╔╝██║   ██║        ██║   ██║     ███████║███████║██║  ██║
    ██╔═══╝ ██╔══██╗██║   ██║        ██║   ██║     ██╔══██║██╔══██║██║  ██║
    ██║     ██║  ██║╚██████╔╝        ██║   ╚██████╗██║  ██║██║  ██║██████╔╝
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝         ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                    STUDENT NETWORK PROTOCOL LABORATORY
                           Communauté Tchadienne
    """)
    print(Style.RESET)


def progress_bar(label, duration=2.0, length=40):
    print(f"\n{Style.CYAN}[*] {label}{Style.RESET}")
    steps = int(length)
    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        bar = '█' * i + '░' * (steps - i)
        sys.stdout.write(f"\r{Style.GREEN}[{bar}] {percent}%{Style.RESET}")
        sys.stdout.flush()
        time.sleep(duration / steps)
    print()


def run_cmd(title, cmd):
    print(f"\n  {Style.BOLD}{Style.YELLOW}{title}{Style.RESET}")
    print(f"  {Style.DARK_GREEN}$ {cmd}{Style.RESET}")
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=15
        )
        if result.stdout:
            print(result.stdout[:1000])
        if result.returncode != 0 and result.stderr:
            print(f"{Style.RED}  {result.stderr[:500]}{Style.RESET}")
    except Exception as e:
        print(f"{Style.RED}  Erreur : {e}{Style.RESET}")


def demo_http():
    print(f"\n{Style.YELLOW}[DÉMO] Requête HTTPS GET vers httpbin.org{Style.RESET}")
    try:
        req = urllib.request.Request(
            'https://httpbin.org/get',
            headers={'User-Agent': 'PRO-TCHAD-STUD/2.0'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read().decode('utf-8')
            print(data[:800])
    except Exception as e:
        print(f"{Style.RED}Erreur : {e}{Style.RESET}")


def demo_tcp():
    print(f"\n{Style.YELLOW}[DÉMO] Client TCP vers google.com:443{Style.RESET}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect(('google.com', 443))
        print(f"{Style.GREEN}[+] Connecté à google.com:443{Style.RESET}")
        print(f"{Style.CYAN}    Local: {s.getsockname()}{Style.RESET}")
        print(f"{Style.CYAN}    Distant: {s.getpeername()}{Style.RESET}")
        s.close()
    except Exception as e:
        print(f"{Style.RED}Erreur : {e}{Style.RESET}")


def demo_udp():
    print(f"\n{Style.YELLOW}[DÉMO] Envoi UDP vers 8.8.8.8:53{Style.RESET}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(2)
        s.sendto(b'hello', ('8.8.8.8', 53))
        print(f"{Style.GREEN}[+] Paquet UDP envoyé{Style.RESET}")
        try:
            data, addr = s.recvfrom(1024)
            print(f"{Style.CYAN}    Réponse de {addr}: {data[:50]}{Style.RESET}")
        except socket.timeout:
            print(f"{Style.YELLOW}[!] Pas de réponse (normal avec UDP non sollicité){Style.RESET}")
        s.close()
    except Exception as e:
        print(f"{Style.RED}Erreur : {e}{Style.RESET}")


def demo_dns():
    print(f"\n{Style.YELLOW}[DÉMO] Résolution DNS avec socket.getaddrinfo{Style.RESET}")
    try:
        results = socket.getaddrinfo('google.com', None)
        print(f"{Style.GREEN}[+] Résolutions trouvées pour google.com :{Style.RESET}")
        for r in results[:5]:
            family, _, _, _, sockaddr = r
            ip_type = 'IPv6' if family == socket.AF_INET6 else 'IPv4'
            print(f"{Style.CYAN}    {sockaddr[0]} ({ip_type}){Style.RESET}")
    except Exception as e:
        print(f"{Style.RED}Erreur : {e}{Style.RESET}")


def demo_icmp():
    print(f"\n{Style.YELLOW}[DÉMO] Ping ICMP vers 1.1.1.1{Style.RESET}")
    try:
        result = subprocess.run(
            ['ping', '-c', '3', '1.1.1.1'],
            capture_output=True, text=True, timeout=15
        )
        print(result.stdout)
    except Exception as e:
        print(f"{Style.RED}Erreur : {e}{Style.RESET}")


def demo_arp():
    print(f"\n{Style.YELLOW}[DÉMO] Table ARP locale{Style.RESET}")
    try:
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True, timeout=10)
        print(result.stdout[:800])
    except Exception as e:
        print(f"{Style.RED}Erreur : {e}{Style.RESET}")


def demo_dhcp():
    print(f"\n{Style.YELLOW}[DÉMO] Informations DHCP{Style.RESET}")
    try:
        result = subprocess.run(['ip', 'addr'], capture_output=True, text=True, timeout=10)
        print(result.stdout[:800])
    except Exception as e:
        print(f"{Style.RED}Erreur : {e}{Style.RESET}")


# ==== CATALOGUE DES PROTOCOLES ====
PROTOCOLS = {
    '1': {
        'category': 'Couche Réseau',
        'name': 'IP (IPv4 / IPv6)',
        'desc': 'Adressage logique des hôtes sur Internet.',
        'commands': [
            ("Afficher l'IP locale", "ip addr"),
            ("Afficher la route", "ip route"),
            ("Test IPv6", "ping -6 -c 3 google.com"),
            ("Infos interface", "ip -s link"),
        ],
        'demo': lambda: run_cmd("Adresses IP locales", "ip addr")
    },
    '2': {
        'category': 'Couche Réseau',
        'name': 'ICMP',
        'desc': 'Diagnostic réseau : ping, traceroute, MTU.',
        'commands': [
            ("Ping", "ping -c 4 1.1.1.1"),
            ("Traceroute", "traceroute google.com"),
            ("Path MTU", "ping -c 4 -M do -s 1472 google.com"),
            ("Ping IPv6", "ping6 -c 4 google.com"),
        ],
        'demo': demo_icmp
    },
    '3': {
        'category': 'Couche Réseau',
        'name': 'ARP / RARP',
        'desc': 'Association adresse IP ↔ adresse MAC.',
        'commands': [
            ("Table ARP", "arp -a"),
            ("Résoudre MAC", "arp -n 192.168.1.1"),
            ("Vider ARP", "sudo ip -s -s neigh flush all"),
        ],
        'demo': demo_arp
    },
    '4': {
        'category': 'Couche Réseau',
        'name': 'IGMP',
        'desc': 'Gestion des groupes multicast.',
        'commands': [
            ("Groupes multicast", "ip maddr"),
            ("Route multicast", "ip mroute"),
        ],
        'demo': lambda: run_cmd("Adresses multicast", "ip maddr")
    },
    '5': {
        'category': 'Couche Réseau',
        'name': 'NDP (IPv6)',
        'desc': 'Neighbor Discovery Protocol pour IPv6.',
        'commands': [
            ("Voisins IPv6", "ip -6 neigh"),
            ("Route IPv6", "ip -6 route"),
        ],
        'demo': lambda: run_cmd("Voisins IPv6", "ip -6 neigh")
    },
    '6': {
        'category': 'Couche Transport',
        'name': 'TCP',
        'desc': 'Connexion fiable, orientée flux.',
        'commands': [
            ("Tester port TCP", "nc -vz google.com 443"),
            ("Connexions actives", "ss -tuln"),
            ("Capturer paquets TCP", "sudo tcpdump -i any -c 10 tcp"),
        ],
        'demo': demo_tcp
    },
    '7': {
        'category': 'Couche Transport',
        'name': 'UDP',
        'desc': 'Rapide, sans connexion.',
        'commands': [
            ("Tester port UDP", "nc -vzu 8.8.8.8 53"),
            ("Sockets UDP", "ss -uln"),
            ("Envoyer UDP", "echo 'test' | nc -u 127.0.0.1 5005"),
        ],
        'demo': demo_udp
    },
    '8': {
        'category': 'Couche Transport',
        'name': 'SCTP / DCCP / QUIC',
        'desc': 'Protocoles alternatifs de transport.',
        'commands': [
            ("SCTP associations", "ss -S"),
            ("QUIC test", "curl --http3 -I https://cloudflare-quic.com"),
            ("Infos TCP/QUIC", "ss -tin"),
        ],
        'demo': lambda: print(f"{Style.YELLOW}[INFO] QUIC nécessite curl avec support HTTP/3.{Style.RESET}")
    },
    '9': {
        'category': 'Routage',
        'name': 'BGP / OSPF / RIP / IS-IS / EIGRP',
        'desc': 'Protocoles de routage dynamique.',
        'commands': [
            ("Table de routage", "ip route"),
            ("Route BGP publique", "whois -h whois.radb.net '136.1.0.0/16'"),
            ("Traceroute AS", "mtr --report google.com"),
        ],
        'demo': lambda: run_cmd("Table de routage", "ip route")
    },
    '10': {
        'category': 'Attribution d\'adresses',
        'name': 'DHCP / BOOTP',
        'desc': 'Attribution automatique des adresses IP.',
        'commands': [
            ("Renouveler bail", "sudo dhclient -r && sudo dhclient"),
            ("Baux DHCP", "cat /var/lib/dhcp/dhclient.leases"),
            ("Découverte DHCP", "sudo nmap --script broadcast-dhcp-discover"),
        ],
        'demo': demo_dhcp
    },
    '11': {
        'category': 'Résolution de noms',
        'name': 'DNS / mDNS / LLMNR',
        'desc': 'Traduction nom ↔ IP.',
        'commands': [
            ("Dig A", "dig google.com A"),
            ("Dig MX", "dig google.com MX"),
            ("Trace DNS", "dig +trace google.com"),
            ("mDNS", "avahi-browse -a"),
        ],
        'demo': demo_dns
    },
    '12': {
        'category': 'Web',
        'name': 'HTTP / HTTPS / HTTP/2 / HTTP/3 / WebSocket',
        'desc': 'Protocoles du World Wide Web.',
        'commands': [
            ("GET", "curl -I https://www.google.com"),
            ("HTTP/2", "curl --http2 -I https://www.google.com"),
            ("HTTP/3", "curl --http3 -I https://cloudflare-quic.com"),
            ("WebSocket", "wscat -c wss://echo.websocket.org"),
        ],
        'demo': demo_http
    },
    '13': {
        'category': 'Transfert de fichiers',
        'name': 'FTP / FTPS / SFTP / TFTP / SCP / Rsync',
        'desc': 'Transfert de fichiers sur réseau.',
        'commands': [
            ("FTP", "ftp utilisateur@serveur"),
            ("SFTP", "sftp utilisateur@serveur"),
            ("SCP", "scp fichier.txt user@host:/path"),
            ("Rsync", "rsync -avz source/ dest/"),
        ],
        'demo': None
    },
    '14': {
        'category': 'Courrier électronique',
        'name': 'SMTP / POP3 / IMAP',
        'desc': 'Envoi et réception d\'emails.',
        'commands': [
            ("Test SMTP", "telnet smtp.gmail.com 587"),
            ("Test IMAP SSL", "openssl s_client -connect imap.gmail.com:993"),
            ("Test POP3 SSL", "openssl s_client -connect pop.gmail.com:995"),
        ],
        'demo': None
    },
    '15': {
        'category': 'Accès distant',
        'name': 'SSH / Telnet / RDP / VNC',
        'desc': 'Connexion et contrôle à distance.',
        'commands': [
            ("SSH", "ssh user@host"),
            ("SSH tunnel", "ssh -L 8080:localhost:80 user@host"),
            ("VNC", "vncviewer host:5900"),
            ("RDP", "xfreerdp /v:host /u:user"),
        ],
        'demo': None
    },
    '16': {
        'category': 'Sécurité',
        'name': 'TLS / IPsec / Kerberos / OAuth 2.0 / OpenID Connect',
        'desc': 'Sécurisation des communications et authentification.',
        'commands': [
            ("Certificat TLS", "openssl s_client -connect google.com:443 -servername google.com"),
            ("Ciphers TLS", "nmap --script ssl-enum-ciphers -p 443 google.com"),
            ("TGT Kerberos", "klist"),
            ("OAuth flow", "curl https://accounts.google.com/.well-known/openid-configuration"),
        ],
        'demo': None
    },
    '17': {
        'category': 'Synchronisation',
        'name': 'NTP / PTP',
        'desc': 'Synchronisation temporelle.',
        'commands': [
            ("Date NTP", "ntpdate -q pool.ntp.org"),
            ("Statut NTP", "timedatectl status"),
            ("Serveurs NTP", "cat /etc/ntp.conf"),
        ],
        'demo': lambda: run_cmd("Statut de l'heure", "timedatectl status")
    },
    '18': {
        'category': 'Voix et vidéo',
        'name': 'SIP / RTP / RTCP / RTSP / WebRTC',
        'desc': 'Streaming multimédia et VoIP.',
        'commands': [
            ("Infos SIP", "sipcalc 192.168.1.0/24"),
            ("Ports RTP", "ss -uln | grep -E '5060|10000:20000'"),
            ("WebRTC test", "curl https://webrtc.github.io/samples/"),
        ],
        'demo': None
    },
    '19': {
        'category': 'Réseaux sans fil',
        'name': 'Wi-Fi / Bluetooth / Zigbee / Z-Wave / LoRaWAN / NFC',
        'desc': 'Communication sans fil.',
        'commands': [
            ("Wi-Fi", "iw dev"),
            ("Scan Wi-Fi", "sudo iwlist scan"),
            ("Bluetooth", "bluetoothctl devices"),
            ("NFC", "nfc-list"),
        ],
        'demo': lambda: run_cmd("Interfaces sans fil", "iw dev")
    },
    '20': {
        'category': 'Internet des objets (IoT)',
        'name': 'MQTT / CoAP / AMQP / DDS / XMPP',
        'desc': 'Protocoles machine-to-machine.',
        'commands': [
            ("MQTT subscribe", "mosquitto_sub -h test.mosquitto.org -t '#' -C 5"),
            ("MQTT publish", "mosquitto_pub -h test.mosquitto.org -t 'test' -m 'hello'"),
            ("AMQP", "curl -u guest:guest http://localhost:15672/api/overview"),
        ],
        'demo': None
    },
    '21': {
        'category': 'Annuaire',
        'name': 'LDAP / LDAPS',
        'desc': 'Services d\'annuaire.',
        'commands': [
            ("Test LDAP", "ldapsearch -x -H ldap://ldap.example.com -b dc=example,dc=com"),
            ("LDAPs", "ldapsearch -x -H ldaps://ldap.example.com"),
        ],
        'demo': None
    },
    '22': {
        'category': 'Virtualisation et VPN',
        'name': 'OpenVPN / WireGuard / L2TP / PPTP / GRE',
        'desc': 'Réseaux privés virtuels et tunnels.',
        'commands': [
            ("WireGuard", "wg show"),
            ("Interfaces VPN", "ip link show type wireguard"),
            ("OpenVPN status", "systemctl status openvpn"),
        ],
        'demo': lambda: run_cmd("Interfaces réseau", "ip link")
    },
    '23': {
        'category': 'Gestion réseau',
        'name': 'SNMP / NetFlow / Syslog',
        'desc': 'Supervision et collecte de logs.',
        'commands': [
            ("SNMP walk", "snmpwalk -v2c -c public 192.168.1.1"),
            ("Syslog", "tail -n 20 /var/log/syslog"),
            ("Journal", "journalctl -n 20"),
        ],
        'demo': lambda: run_cmd("Dernières logs", "journalctl -n 10 || tail -n 10 /var/log/syslog")
    },
    '24': {
        'category': 'Industriel',
        'name': 'Modbus / OPC UA / CAN Bus / DNP3 / BACnet / PROFIBUS / EtherCAT',
        'desc': 'Protocoles industriels et SCADA.',
        'commands': [
            ("Modbus TCP", "mbtget -r3 -a 1 -n 10 192.168.1.100"),
            ("CAN dump", "candump can0"),
            ("OPC UA discovery", "uascan -u opc.tcp://host:4840"),
        ],
        'demo': None
    },
}


# ==== MENU ====
def show_menu():
    print(f"\n{Style.BOLD}{Style.UNDERLINE}MENU DES PROTOCOLES{Style.RESET}\n")
    current_category = None
    for key, proto in PROTOCOLS.items():
        if proto['category'] != current_category:
            current_category = proto['category']
            print(f"\n{Style.MAGENTA}{Style.BOLD}[ {current_category} ]{Style.RESET}")
        print(f"{Style.GREEN}[{key}]{Style.RESET} {Style.CYAN}{proto['name']}{Style.RESET}")
    print(f"\n{Style.YELLOW}[0]{Style.RESET} Quitter")
    print(f"{Style.YELLOW}[A]{Style.RESET} Lancer toutes les démos rapides")
    print(f"{Style.YELLOW}[S]{Style.RESET} Mode recherche par mot-clé")


def show_protocol(key):
    proto = PROTOCOLS[key]
    print(f"\n{Style.BOLD}{Style.GREEN}=== {proto['name']} ==={Style.RESET}")
    print(f"{Style.MAGENTA}Catégorie : {proto['category']}{Style.RESET}")
    print(f"{Style.CYAN}{proto['desc']}{Style.RESET}\n")

    print(f"{Style.YELLOW}Commandes pratiques :{Style.RESET}")
    for i, (title, cmd) in enumerate(proto['commands'], 1):
        print(f"  {Style.GREEN}{i}.{Style.RESET} {Style.BOLD}{title}{Style.RESET}")
        print(f"     {Style.DARK_GREEN}$ {cmd}{Style.RESET}\n")

    if proto['demo']:
        choice = input(f"{Style.CYAN}Lancer la démo ? (o/n) : {Style.RESET}").strip().lower()
        if choice == 'o':
            progress_bar("Initialisation de la démo...", 1.0)
            proto['demo']()

    input(f"\n{Style.YELLOW}Appuyez sur Entrée pour revenir au menu...{Style.RESET}")


def run_all_demos():
    progress_bar("Lancement de toutes les démos", 2.0)
    for key, proto in PROTOCOLS.items():
        if proto['demo']:
            print(f"\n{Style.BOLD}{Style.GREEN}[{key}] {proto['name']}{Style.RESET}")
            proto['demo']()
            time.sleep(0.5)
    input(f"\n{Style.YELLOW}Appuyez sur Entrée pour revenir au menu...{Style.RESET}")


def search_protocols():
    keyword = input(f"{Style.CYAN}Mot-clé à rechercher : {Style.RESET}").strip().lower()
    print(f"\n{Style.YELLOW}Résultats pour '{keyword}' :{Style.RESET}")
    found = False
    for key, proto in PROTOCOLS.items():
        if keyword in proto['name'].lower() or keyword in proto['category'].lower() or keyword in proto['desc'].lower():
            print(f"{Style.GREEN}[{key}]{Style.RESET} {Style.CYAN}{proto['name']}{Style.RESET} ({proto['category']})")
            found = True
    if not found:
        print(f"{Style.RED}Aucun protocole trouvé.{Style.RESET}")
    input(f"\n{Style.YELLOW}Appuyez sur Entrée...{Style.RESET}")


def main():
    banner()
    progress_bar("Initialisation de PRO-TCHAD-STUD v2.0", 2.0)
    typing(f"{Style.GREEN}[+] Plateforme prête. 60+ protocoles à explorer.{Style.RESET}", 0.02)

    while True:
        banner()
        show_menu()
        choice = input(f"\n{Style.CYAN}Votre choix : {Style.RESET}").strip().upper()

        if choice == '0':
            typing(f"{Style.GREEN}[+] Fermeture de PRO-TCHAD-STUD. À bientôt !{Style.RESET}", 0.02)
            break
        elif choice == 'A':
            run_all_demos()
        elif choice == 'S':
            search_protocols()
        elif choice in PROTOCOLS:
            show_protocol(choice)
        else:
            print(f"{Style.RED}[-] Choix invalide.{Style.RESET}")
            time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Style.GREEN}[+] Interrompu par l'utilisateur.{Style.RESET}")

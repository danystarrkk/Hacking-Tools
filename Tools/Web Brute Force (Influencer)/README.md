Este script creado en Python3 para poder realizar el ataque de fuerza bruta al panel de WordPress en la máquina (Influencer).

El script está adaptado para poder replicar y auditar este tipo de comportamientos en cualquier entorno controlado o laboratorio de pruebas.

# [+] Uso:

Los parámetros son:

- `-u` Le pasamos el usuario a atacar.
- `-w` Le pasamos el diccionario de palabras a utilizar.
- `-m` Le pasamos la url del panel de WordPress.

Ejemplo:

```bash
python3 bruteforce.py -u luna -w ../cupp/luna.txt -m http://192.168.56.3/wordpress/wp-login.php
```

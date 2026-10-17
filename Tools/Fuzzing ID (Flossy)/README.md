Este es un script programado en Python3 que permite realizar una enumeración de identificadores (IDs) mediante consultas estructuradas (GraphQL) para identificar usuarios activos y extraer sus respectivas credenciales (usuario y contraseña).

El script está adaptado para poder replicar y auditar este tipo de comportamientos en cualquier entorno controlado o laboratorio de pruebas.

# [+] Uso:

Los parámetros son:

- `-u`, `--url` : Para definir la URL del endpoint objetivo (Ejemplo: `-u http://192.168.74.130/api`).
- `-r`, `--rango` : Para definir el rango de IDs a evaluar (Ejemplo: `-r 1-100`).

Ejemplo de uso:

```bash
python3 script.py -u <URL> -r <RANGO>
```

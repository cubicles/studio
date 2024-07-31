# README pls

- El __init__.py puede ser dejado en blanco
- El .py/script que llama a la ejecución tiene que estar a nivel del package (from package import module)
- El package seria el nombre del folder y el module el nombre del .py
- En caso el .py/script que llama la ejecucion no este a nivel del package se debe realizar
un sys append. Esto se puede ver en scripts/main:
"sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')"

#!/usr/bin/python3
"""reducer.py"""

import sys

max_id = 0
max_total = 0
last_key = None

for line in sys.stdin:
    line = line.strip()
    values = line.split(':')
    id_sucursal, id_producto, total_vendido = values

    if last_key == id_sucursal:
        total_vendido = int(total_vendido)
        if total_vendido > max_total:
            max_id = id_producto
            max_total = total_vendido
    else:
        if last_key:
            print("%s:%s:%s" % (id_sucursal, max_id, max_total))
        max_id = id_producto
        max_total = int(total_vendido)
        last_key = id_sucursal

if last_key == id_sucursal:
    print("%s:%s:%s" % (id_sucursal, max_id, max_total))

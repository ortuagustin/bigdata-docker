#!/usr/bin/python3
"""reducer.py"""

import sys

productos_distintos = {}
max_sucursal_distintos = 0
max_id_sucursal_distintos = 0
max_id_producto = 0
max_producto = 0
last_key = None

for line in sys.stdin:
    line = line.strip()
    values = line.split(':')
    id_sucursal, id_producto, total_vendido = values

    if last_key == id_sucursal:

        total_vendido = int(total_vendido)
        if total_vendido > max_producto:
            max_id_producto = id_producto
            max_producto = total_vendido

        productos_distintos[id_producto] = 1
        if len(productos_distintos) > max_sucursal_distintos:
            max_sucursal_distintos = len(productos_distintos)
            max_id_sucursal_distintos = id_sucursal
    else:
        if last_key:
            print("%s:%s:%s" % (id_sucursal, max_id_producto, max_producto))

        max_id_producto = id_producto
        max_producto = int(total_vendido)

        productos_distintos = {}
        max_id_sucursal_distintos = id_sucursal

        last_key = id_sucursal

if last_key == id_sucursal:
    print("%s:%s:%s" % (id_sucursal, max_id_producto, max_producto))

print("%s:%s" % (max_sucursal_distintos, max_id_sucursal_distintos))

#!/usr/bin/python3
"""reducer.py"""

import sys

last_key = None
for line in sys.stdin:
    line = line.strip()
    values = line.split(':', 2)
    id_sucursal, id_producto, cantidad_vendida = values
    key = (id_sucursal, id_producto)

    if last_key == key:
        sum += int(cantidad_vendida)
    else:
        if last_key:
            print("%s:%s:%s" % (last_key[0], last_key[1], sum))
        sum = int(cantidad_vendida)
        last_key = key

if last_key == key:
    print("%s:%s:%s" % (last_key[0], last_key[1], sum))

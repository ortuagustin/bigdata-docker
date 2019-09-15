#!/usr/bin/python3
"""mapper.py"""

## map (key, value)
# j1 write ((suc, prod), cant)
# -----------
# j2  write (suc, (prod, sumatoria))

## reduce(key, values)
# j1 write(key, sum)
# -----------
# j2  write (suc, prod, max)

import sys

for line in sys.stdin:
    line = line.strip()
    value = line.split()
    id_sucursal, id_producto, cantidad_vendida = value

    print('%s:%s:%s' % (id_sucursal, id_producto, cantidad_vendida))

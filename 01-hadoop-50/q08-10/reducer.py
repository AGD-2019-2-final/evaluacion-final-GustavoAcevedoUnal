#!/usr/bin/env python

import sys

if __name__ == '__main__':

    curkey = None
    i = 0
    suma = 0
    prom = 0

    for line in sys.stdin:
        key, val = line.split("\t")
        val = float(val)
        
        if curkey is None:
            curkey = key
        
        if key == curkey:
              suma += val
              i += 1
        else:
            prom = suma / i
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, prom))
            
            i = 0
            i += 1
            suma = 0
            suma += val
            curkey = key
            
    prom = suma / i       
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, prom))

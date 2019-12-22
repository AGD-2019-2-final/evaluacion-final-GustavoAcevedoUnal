#!/usr/bin/env python

import sys

if __name__ == '__main__':
    lista = []
    for line in sys.stdin:
        key, val1, val2 = line.split("\t")
        lista.append([key,val1,int(val2.strip())])
    
    lista = sorted(lista, key=lambda x: x[2])[:6]
    for line in lista:
        sys.stdout.write("{}\t{}\t{}\n".format(line[0], line[1], line[2]))

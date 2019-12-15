#!/usr/bin/env python

import sys

if __name__ == '__main__':
    for line in sys.stdin:
      line = line.strip()
      key_columna = line.split(',')[1]
      valor_columna = line.split(',')[0]
      sys.stdout.write("{},{}\n".format(key_columna,valor_columna))

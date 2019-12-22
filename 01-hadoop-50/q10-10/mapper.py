#! /usr/bin/env python

import sys
if __name__ == "__main__":
    for line in sys.stdin:
      key_columna = line.split('\t')[0]
      valor_columna = line.split('\t')[1].strip()
      sys.stdout.write("{}\t{}\n".format(key_columna,valor_columna))

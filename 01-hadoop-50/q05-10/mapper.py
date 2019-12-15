#! /usr/bin/env python

import sys
if __name__ == "__main__":
    for line in sys.stdin:
      key_columna = line.split('   ')[1].split('-')[1]
      valor_columna = 1
      sys.stdout.write("{}\t{}\n".format(key_columna,valor_columna))

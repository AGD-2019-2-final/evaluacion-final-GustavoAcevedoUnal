#! /usr/bin/env python

import sys
if __name__ == "__main__":
    for line in sys.stdin:
      key_columna = line.split('   ')[0]
      valor1_columna = line.split('   ')[1]
      valor2_columna = line.split('   ')[2].strip()
      sys.stdout.write("{}\t{}\t{}\n".format(key_columna,valor1_columna,valor2_columna))

#!/usr/bin/env python
# -*- coding: utf8 -*-
# Python 3.8
# Get Rabdin nac to clipboard

import pyperclip as clipboard
import random
import msvcrt

def randomMAC():
    return [ 0x02, 0x16, 0x3e,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]

def MACprettyprint(mac):
    return '-'.join(map(lambda x: "%02x" % x, mac))

if __name__ == '__main__':
    x = (MACprettyprint(randomMAC()).upper())
    clipboard.copy(x)
    """
    print x
    print("Copiado, presione tecla para cerrar")
    msvcrt.getch()
"""
"""
import msvcrt

print("Presione 'ñ' para continuar...")
key = None
while key != 'ñ':
    key = msvcrt.getwch()
"""

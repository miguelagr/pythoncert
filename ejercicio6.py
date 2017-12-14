#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

numod = {n:[hex(n),bin(n)] for n in range(50) if bin(n).count('1') % 2 != 0}

print numod

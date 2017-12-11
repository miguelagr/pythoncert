#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

{n:(bin(n),hex(n)) for n in range(50) if bin(n).count('1') % 2 !=0}	

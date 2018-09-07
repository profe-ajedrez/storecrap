#!python3
# -*- coding: utf-8 -*-
"""
Store Craper
v 0.1.1

Script que registra variaciones de precios de productos en
multitiendas chilenas
Licencia GPL2 no comercial
EULA para uso comercial

@author: Andrés Reyes a.k.a. jacobopus
website http://jacobopus.github.io
2018

Requiere

BeautifulSoup
request_html

Changelog

v 012 Refactorización de código.
v 011 behaviour paginacion
v 010 utilidad de recuperación de url categorias y bug fixes
v 001 implementation with Pyhon-Request instead of plane Python 3
"""

import settings
import data_sources
import page_behaviours


page_behaviours.target_loop(data_sources.targets['falabella'])

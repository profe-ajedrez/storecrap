#!/usr/bin/env python3
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

Dependencias

BeautifulSoup
request_html

Changelog
v0.1.6 07/09/2018 encapsulación de comportamoento de paginas de categorias en clases respectivas. OOPdización. Github
v0.1.5 07/09/2018 erased by error (Epic fail!)
v0.1.4 07/09/2018 Limpieza código
v0.1.3 fixes
v0.1.2
v0.1.1
v0.1.0
v0.0.1 05/09/2018 implementation with Pyhon-Request instead of plane Python 3
"""

import settings
import data_sources
import target_loop
import utils
import scrape_tools

db = {}

db['falabella'] = target_loop.target_loop(data_sources.targets['falabella'])

scrape_tools.save_productos(db)
utils.check_kill_process('chrome')

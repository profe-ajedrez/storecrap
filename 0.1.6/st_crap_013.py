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

Requiere

BeautifulSoup
request_html

Changelog
v 0.1.3 fixes
v 0.1.2
v 0.1.1
v 0.1.0
v 0.0.1 implementation with Pyhon-Request instead of plane Python 3
"""

import settings
import data_sources
import page_behaviours_013
import utils


page_behaviours_013.target_loop(data_sources.targets['falabella'])
utils.check_kill_process('chrome')
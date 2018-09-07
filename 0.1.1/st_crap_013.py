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

v 012
v 011
v 010
v 001 implementation with Pyhon-Request instead of plane Python 3
"""

import settings
import data_sources
import page_behaviours_013


page_behaviours_013.target_loop(data_sources.targets['falabella'])
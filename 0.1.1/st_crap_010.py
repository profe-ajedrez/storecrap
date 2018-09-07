#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Store Craper
v 0.1.0

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
implementation with Pyhon-Request instead of plane Python 3
"""
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import settings
import scrape_tools
import utils

# Indico que estamos en fase de produccion
utils.environment = utils.development
session = HTMLSession()

for key in settings.targets.keys():
    
    print('Iniciando proceso target ' + key)
    site = scrape_tools.render_html(session,
                                    settings.targets[key]['base-url'])

    links = scrape_tools.remove_unneeded_links(site.html.absolute_links, 
                                               settings.targets[key]['keyword'])
     

    for link in links:
        #category_site = scrape_tools.render_html(session, link)
        utils.debug_log(link)
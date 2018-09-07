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
implementation with Pyhon-Request instead of plane Python 3
"""
from requests_html import HTMLSession
from requests_html import MaxRetries
from bs4 import BeautifulSoup
import json
import re
import settings
import scrape_tools
import utils
import data_sources


# Indico que estamos en fase de desarrollo
utils.environment = utils.development
session = HTMLSession()
print('.' + data_sources.targets['falabella']['css-selector'])

try:
    print("contactando target")
    product_site = session.get('https://www.falabella.com/falabella-cl/category/cat720161/Smartphones')
    print("intentando renderizar")
    product_site.html.render(wait=2, sleep=2)
    print("recuperando...")
    productos_html = product_site.html.find('div.' + data_sources.targets['falabella']['css-selector'])    
    
    print("Construyendo listas")
    productos = []
    for p in productos_html:
        pp = p.html    
        bs = BeautifulSoup(pp, 'html.parser')
        producto = {}
        producto['marca'] = bs.find("div", {"class": "section__pod-top-brand"}).text
        producto['articulo'] = bs.find("div", {"class": "section__pod-top-title"}).text
        raw_values = bs.find_all("p", {"class": "fb-price"})

        
        precios = []
        for raw_value in raw_values:
            
            precios.append(re.sub('[^0-9]','', raw_value.text))
       
        producto['valores'] = precios
        
        productos.append(producto)


    print(productos)
    json = json.dumps(productos)
    f = open("dict.json","w")
    f.write(json)
    f.close()    
    
except MaxRetries:
    print('no se puede renderizar la pagina, compruebe la url proporcionada e intente en unos minutos')
    

    




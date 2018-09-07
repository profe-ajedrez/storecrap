#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
from requests_html import HTMLSession
from requests_html import MaxRetries
from bs4 import BeautifulSoup
import json
import re
import datetime
import settings
import scrape_tools
import utils
import data_sources


def  target_loop(target, file_name=''):
    '''
    
    '''
    session = HTMLSession()
    categorias = target['categorias']
    productos = []
    
    for categoria, url in categorias.items():
        
            print('Procesando categoria ' + categoria)
            print('url : ' + url)
            
            try:
                category_page = scrape_tools.render_html(session, url)
            
            except MaxRetries:
                print('no se puede renderizar la pagina, compruebe la url proporcionada e intente en unos minutos')
                
            print('recuperando')   

            for page in category_page.html:
                bs = BeautifulSoup(page, 'html.parser')
                raw_products = bs.find_all(target['html-container'], {target['selector-type']: target['css-selector']})
                marcas =  bs.find_all(target['html-container'], {target['selector-type']: target['css-brand-selector']})
                articulos = bs.find_all(target['html-container'], {target['selector-type']: target['css-item-selector']})
                precios = bs.find_all(target['html-container'], {target['selector-type']: target['css-precio-selector']}) 
                
                i = 0
                for p in articulos:
                    dp = {}
                    dp['marca'] = marcas[i]
                    dp['articulo'] = p
                    
                    valores = []
                    for precio in precios[i]:
                        valores.append(re.sub('[^0-9]','', precio.text))
                        
                    dp['precios'] = valores
                    
                    if dp not in productos:
                        productos.append[db]
                        
                    i += 1
        
    print('guardando productos target : ' + target['nombre'])
    if file_name.strip == '':
        now = datetime.datetime.now()
        file_name = 'target_' + target['nombre'] + '_' + now.isoformat()
        
    json_dump = json.dumps(productos)
    with open(file_name, "w") as f:
        f.write(json)
        print('exito al guardar')

    '''
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
   '''

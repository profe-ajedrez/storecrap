#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 07:44:14 2018

@author: jacobopus
"""
import re
from requests_html import HTMLSession
from requests_html import MaxRetries
from bs4 import BeautifulSoup
import datetime
import math
import json
import settings
import utils


def render_html(session, url):
    '''
    renderiza la pagina web si está construida a base de
    fuerte uso de javascript
    '''
    try:
        print('contactando target')
        site = session.get(url)
        print('intentando renderizar, esto puede tardar un rato')
        site.html.render(sleep=2, retries=3)
        
    except MaxRetries:
        print('no se puede renderizar la pagina, compruebe la url proporcionada e intente en unos minutos')
        return None
    
    except:
        print('no se puede renderizar la pagina, compruebe su conexión a internet y la url proporcionada e intente en unos minutos')
        return None        
    return site

def next(site):
    pg = None
    for pg in site.html:
        break    
    return pg


def get_next_page_soap(num_page=1, session=None, nueva_conexion=False, uri=''):
    '''
    Devuelve el objeto BeautifulSoap de la url paginada indicada por num_page
    '''
    n_p = str(num_page + 1)
    uri += n_p
    print('intentando descargar pagina n° ' + n_p)
    
    if (nueva_conexion or session is None):
        session = HTMLSession()
        
    page = render_html(session, uri)
    if page is None:
        return None
    pg = next(page)
    if pg is None:
        return None
    
    soap = BeautifulSoup(pg.html, 'html.parser')    
    return soap

def get_integer(soap, selector, target_name=''):
    '''
    Convierte a integer el contenido de un selector obtenido a traves de bs4 y lo devuelve.
    '''
    tmp_num = soap.select_one(selector).get_text(strip=True)
    print(tmp_num)
    
    if target_name == 'Falabella':
        tmp_num = num_falabella(tmp_num)
        
    num = int(tmp_num)
    return num
    
def num_falabella(html):
    '''
    Encuentra en html el numero de productos segun la estructura de falabella
    '''
    i = html.index('de')
    f = html.index('resultado')
    num = html[i +2: f-1]
    return num


def remove_unneeded_links(listaLinks, keyword=''):
    '''
    Remueve los enlaces contenidos en listaLinks que no contienen la keyword
    '''
    urls = []
    for link in listaLinks:

        if keyword in link:
            if link not in urls:
                urls.append(link)

    return urls


def get_num_pages(soap, target):
    total_prods = get_integer(soap, 
                              target['selector-cantidad'],
                              target['nombre'])
    raw_num_products = soap.find_all(target['html-container'], 
                                     {target['selector-type']: target['css-selector']})
    
    num_pages = math.floor(total_prods / len(raw_num_products)) + 2    
    return num_pages


def add_products(target, soap, productos):
    '''
    
    '''
    marcas =  soap.find_all(target['html-container'], {target['selector-type']: target['css-brand-selector']})
    articulos = soap.find_all(target['html-container'], {target['selector-type']: target['css-item-selector']})
    precios = soap.find_all(target['html-container'], {target['selector-type']: target['css-precio-selector']})

    i = 0
    max_index = len(articulos) 
    for i in range(0, max_index):    
        dp = {}
        if target['css-brand-selector'] == 'none':
            dp['marca'] = 'Sin info'
        else:    
            dp['marca'] = marcas[i].text
        
        dp['articulo'] = articulos[i].text

        valores = []
        for precio in precios[i]:
            valores.append(re.sub('[^0-9]','', precio.text))

        dp['precios'] = valores
        productos.append(dp)
        print('agregado producto ' + dp['articulo'])
    i += 1

    return i


def save_productos(productos, file_name=''):
    if len( productos) > 0:
        print('guardando productos')
        if file_name.strip:
            now = datetime.datetime.now()
            file_name = settings.directory + '/' + 'log_' + now.isoformat().strip() + '.log'

        print(file_name)
        json_dump = json.dumps(productos)
        with open(file_name, "w") as f:
            f.write(json_dump)
            print('exito al guardar')    
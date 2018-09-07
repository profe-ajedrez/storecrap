#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 07:44:14 2018

@author: jacobopus
"""
import re
from bs4 import BeautifulSoup


def render_html(session, url):
    '''
    renderiza la pagina web si esta esta construida a base de
    fuerte uso de javascript
    '''
    
    print('contactando target')
    site = session.get(url)
    print('intentando renderizar, esto puede tardar un rato')
    site.html.render(wait=2, sleep=2)

    return site


def get_next_page_soap(num_page=1, session=None, uri=''):
    '''
    Devuelve el objeto BeautifulSoap de la url paginada indicada por num_page
    '''
    n_p = str(num_page + 1)
    uri += n_p
    print('intentando descargar pagina n° ' + n_p)
    page = render_html(session, uri)
    pg = None
    for pg in page.html:
        break    
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

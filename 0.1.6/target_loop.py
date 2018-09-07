#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
from requests_html import HTMLSession
from requests_html import MaxRetries
from bs4 import BeautifulSoup
import re
import datetime
import time
import math
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

            category_page = None
            category_page = scrape_tools.render_html(session, url)

            if category_page is not None:
                print('recuperando')
                n_prod = 0
                pg = scrape_tools.next(category_page)
                soap = BeautifulSoup(pg.html, 'html.parser')
                num_pages = scrape_tools.get_num_pages(soap, target)
                recuperar_datos = True
                k = 1
                for k in range(1, num_pages):
                    # Si se pudo descargar la pagina correspondiente 
                    if recuperar_datos: 
                        n_prod = scrape_tools.add_products(target, soap, productos)
                        
                    soap = scrape_tools.get_next_page_soap(num_page=k, 
                                                           nueva_conexion=True, 
                                                           uri=url + target['pagination-structure'])
                    recuperar_datos = (soap is not None)
                                               
                    print('esperando para no aburrir servidores')
                    time.sleep(settings.waiting_time)
                    print('retomando...')
                    
                print('Cantidad de productos procesados: ', n_prod)

    return productos
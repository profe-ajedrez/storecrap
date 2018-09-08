#!python3
# -*- coding: utf-8 -*-
"""
"""
from requests_html import HTMLSession
from requests_html import MaxRetries
from bs4 import BeautifulSoup
import settings
import scrape_tools
from behaviours import *


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
            behaviour = FactoryBehaviour.create(target['behaviour'])
            
            if category_page is not None:
                print('recuperando')
                n_prod = behaviour.procesar(category_page, 
                                            productos, 
                                            target, 
                                            url,
                                            settings.waiting_time)
                    
                print('Cantidad de productos procesados: ', n_prod)

    return productos


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
            try:
                category_page = scrape_tools.render_html(session, url)

            except MaxRetries:
                print('no se puede renderizar la pagina, compruebe la url proporcionada e intente en unos minutos')
                return None
            print('recuperando')

            if category_page is not None:
                n_prod = 0
                pg = None
                for pg in category_page.html:
                    break
                soap = BeautifulSoup(pg.html, 'html.parser')
                total_prods = scrape_tools.get_integer(soap, 
                                                       target['selector-cantidad'],
                                                       target['nombre'])
                raw_num_products = soap.find_all(target['html-container'], 
                                                 {target['selector-type']: target['css-selector']})
                
                num_pages = math.floor(total_prods / len(raw_num_products)) + 2
                recuperar_datos = True
                k = 1
                for k in range(1, num_pages):
                    # Si se pudo descargar la pagina correspondiente 
                    if recuperar_datos: 
                        marcas =  soap.find_all(target['html-container'], {target['selector-type']: target['css-brand-selector']})
                        articulos = soap.find_all(target['html-container'], {target['selector-type']: target['css-item-selector']})
                        precios = soap.find_all(target['html-container'], {target['selector-type']: target['css-precio-selector']})

                        i = 0
                        max_index = len(articulos) 
                        for i in range(0, max_index):
                            dp = {}
                            dp['marca'] = marcas[i].text
                            dp['articulo'] = articulos[i].text

                            valores = []
                            for precio in precios[i]:
                                valores.append(re.sub('[^0-9]','', precio.text))

                            dp['precios'] = valores

                            productos.append(dp)
                            print('agregado producto ', n_prod, ' ' + dp['articulo'])
                            i += 1
                            n_prod += 1
                        
                    try:
                        soap = scrape_tools.get_next_page_soap(num_page=k,
                                            nueva_conexion=True,
                                            uri=url + target['pagination-structure'])
                        recuperar_datos = True
                        
                    except MaxRetries:
                        print('no se puede renderizar la pagina, compruebe la url proporcionada e intente en unos minutos')
                        print('continuando con la siguiente')
                        recuperar_datos = False
                        
                    print('esperando por respeto')
                    time.sleep(3)
                    print('retomando...')
                    
                print('Cantidad de productos procesados: ', n_prod)


    if len( productos) > 0:
        print('guardando productos target : ' + target['nombre'])
        if file_name.strip:
            now = datetime.datetime.now()
            file_name = settings.directory + '/target_' + target['nombre'] + '_' + now.isoformat().strip()

        print(file_name)
        json_dump = json.dumps(productos)
        with open(file_name, "w") as f:
            f.write(json_dump)
            print('exito al guardar')

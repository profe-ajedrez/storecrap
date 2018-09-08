#!python3
# -*- coding: utf-8 -*-
"""
"""
from bs4 import BeautifulSoup
import scrape_tools
import time


class BaseBehaviour():
    '''
    '''
    def __init__(self):
        '''
        '''
        
    def procesar(self, site, productos, target, waiting_time):
        '''
        '''
        pass
    
    
    def esperar_entre_conexiones(self, waiting_time, msg, msg2):
        '''
        '''
        print(msg)
        time.sleep(waiting_time)
        print(msg2)         

               
class PaginatedBehaviour(BaseBehaviour):
    '''
    '''
    def get_num_pages(self, soap, target):
        '''
        '''
        return scrape_tools.get_num_pages(soap, target)
    
    
    def procesar(self, site, productos, target, url, waiting_time):
        '''
        '''
        n_prod = 0
        pg = scrape_tools.next(site)
        soap = BeautifulSoup(pg.html, 'html.parser')
        num_pages = self.get_num_pages(soap, target)
        
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
                                       
            self.esperar_entre_conexiones(waiting_time, 
                                     'esperando para no aburrir servidores', 
                                     'retomando...')    
            
        return n_prod
    

class FactoryBehaviour():
    def create(behaviour='BaseBehaviour'):
        if behaviour == 'PaginatedBehaviour':
            return PaginatedBehaviour()
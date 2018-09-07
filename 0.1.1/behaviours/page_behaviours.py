#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jacobopus
"""
import utils
from scrape_tools import render_html
from requests_html import HTMLSession
from bs4 import BeautifulSoup



class BaseSource:
    def __init__(self, options={'base-url': '',
                                                'pagination-structure': '',
                                                'keyword': '',
                                                'categorias': {'smartphones': ''}}):
        '''
        
        '''
        self.base_url = options['base-url']
        self.keyword = options['keyword']
        self.categorias = options['categorias']
        self.css_selector = options['css-selector']
        self.html_container = options['html-container']
        self.selector_type = options['selector-type']
        self.productos = {}
        

class PaginatedSource(BaseSource):
    def __init__(self, options={'base-url': '',
                                                'pagination-structure': '',
                                                'keyword': '',
                                                'categorias': {'smartphones': ''}}):
        '''
        
        '''
    
    def get_products(self, session, categoria=''):
        '''
        
        '''
        html = session.get(categoria)
        productos = html.find('.' + data_sources.targets['falabella']['css-selector'])
        print(products)
    
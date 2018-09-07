#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jacobopus
"""

# 'smartphones':'https://www.falabella.com/falabella-cl/category/cat720161/Smartphones',
targets = {'falabella': {'nombre': 'Falabella',
                                   'behaviour': 'PaginatedBehaviour',
                                   'base-url': 'https://www.falabella.com/falabella-cl/',
                                   'pagination-structure': '?page=',
                                   'keyword': 'category',
                                   'css-selector': 'pod-item',
                                   'html-container': 'div',
                                   'selector-type': 'class',
                                   'css-brand-selector': 'section__pod-top-brand',
                                   'css-item-selector': 'section__pod-top-title',
                                   'css-precio-selector': 'fb-price-list',
                                   'selector-cantidad': 'h2.fb-filters-sort__title > div > p',
                                   'categorias': {'notebooks-gamer': 'https://www.falabella.com/falabella-cl/category/cat2028/Notebooks-Gamers',
                                                  'notebook': 'https://www.falabella.com/falabella-cl/category/cat5860031/Notebooks-Tradicionales',
                                                  'macbooks': 'https://www.falabella.com/falabella-cl/category/cat5860030/MacBooks', 
                                                  'smartphones': 'https://www.falabella.com/falabella-cl/category/cat720161/Smartphones',
                                                  'smarttv': 'https://www.falabella.com/falabella-cl/category/cat3040054/Smart-TV'}
                                   }
                               
               }
#https://www.paris.cl/store/categoria/tecnologia-computadores?cur_pos=500&cur_page=50
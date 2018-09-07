#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 07:44:14 2018

@author: jacobopus
"""


def render_html(session, url):
    '''
    renderiza la paina web si esta esta construida a base de
    fuerte uso de javascript
    '''
    site = session.get(url)
    site.html.render()
    return site


def remove_unneeded_links(listaLinks, keyword=''):
    '''
    Remueve los enlaces contenidos en listaLinks que no contienen a keyword
    '''
    urls = []
    for link in listaLinks:

        if keyword in link:
            if link not in urls:
                urls.append(link)

    return urls

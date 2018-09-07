#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

'''
development = True
production = False
environment = development

def debug_log(msg):
    if environment:
        print(msg)
        
        
def is_http_url(s):
    """
    Returns true if s is valid http url, else false 
    Arguments:
    - `s`:
    """
    if re.match('https?://(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,2})(?:/[\w&%?#-]{1,300})?',s):
        return True
    else:
        return False        
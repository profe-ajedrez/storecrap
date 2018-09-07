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
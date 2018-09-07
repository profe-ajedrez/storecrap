#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from requests_html import HTMLSession
from bs4 import BeautifulSoup
import settings
import scrape_tools
import utils


url = 'https://www.falabella.com/falabella-cl/category/cat70010/Bicicletas-Urbanas'

session = HTMLSession()
cat_site = scrape_tools.render_html(session, url)



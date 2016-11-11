#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


import os
print("j am in "+ os.getcwd())

THEME= 'pelican-twitchy'


AUTHOR = u'DrAnaximandre'
SITENAME = u'Asmall7'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


PLUGINS = ["render_math"]
DEFAULT_METADATA = {
    'status': 'draft',
}
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


THEME= 'pelican-twitchy'
SITESUBTITLE= u'There is a joke in this title and it is bad'

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


# Social widget
SOCIAL = (
	("1 - My a repos", 'https://github.com/DrAnaximandre'),
	("2 - My friend's repos", 'https://github.com/tboquet'))

DEFAULT_PAGINATION = 5


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images/favicon.ico']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ["render_math"]
DEFAULT_METADATA = {
    'status': 'draft',
}

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'}
}

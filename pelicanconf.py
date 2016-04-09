#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michal Valoušek'
SITENAME = u'Tkalci na webu'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'cs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PATH = 'content'
STATIC_PATHS = ['blog', 'images']
THEME = '/src/templates/'
LOCALE = ("cs_CZ.utf8", )
PAGE_PATHS = ['stranky']

# ceske URL adresy
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{category}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{category}/{slug}.html'

PAGE_URL = 'stranky/{slug}/'
PAGE_SAVE_AS = 'stranky/{slug}.html'

CATEGORY_URL = 'kategorie/{slug}.html'
CATEGORY_SAVE_AS = 'kategorie/{slug}.html'

AUTHOR_URL = 'autor/{slug}.html'
AUTHOR_SAVE_AS = 'autor/{slug}.html'

ARCHIVES_SAVE_AS = 'blog.html'
AUTHORS_SAVE_AS = 'autori.html'

CATEGORIES_SAVE_AS = 'kategorie.html'
TAGS_SAVE_AS = 'tagy.html'

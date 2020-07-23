#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#THEME = 'astrochelys'
THEME = 'astrochelys'
AUTHOR = 'Ogden Boone'
SITENAME = 'test site # 1'
SITEURL = ''

PATH = 'content'
#STATIC_PATHS = ['content/pages/web_dev/testing/images']

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

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

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ["../pelican-plugins",]
PLUGINS = ['extract_toc','pandoc_reader','category_meta']

# settings added by jeff

USE_FOLDER_AS_CATEGORY = True
#READERS = {'md': MARKDOWN, PandocReader}
# MARKDOWN = {
#   'extension_configs': {
#     'markdown.extensions.toc': {}
#   }
# }


# The next two parameters provide input to pandoc_reader
# Additional command line parameters can be passed to pandoc via the PANDOC_ARGS parameter.

PANDOC_ARGS = [
  #'--mathjax',
  '--filter=pandoc-citeproc',
  '--filter=pandoc-sidenote',
  '--lua-filter=./notesymbol.lua',
  '--katex=https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/',
  '--toc',
  '-s',
  '--toc-depth=3',
  '--number-sections',
  '--template=pelican.html',
]

# Pandoc's markdown extensions can be enabled or disabled via the PANDOC_EXTENSIONS parameter.

PANDOC_EXTENSIONS = [
  '-hard_line_breaks',
  '+citations'
]

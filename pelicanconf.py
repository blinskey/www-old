#!/usr/bin/env python

import datetime

AUTHOR = "Benjamin Linskey"
SITENAME = "Benjamin Linskey"
SITEURL = ""

DEFAULT_DATE = "fs"

PATH = "content"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["notes"]
STATIC_PATHS = ["."]

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

DIRECT_TEMPLATES = ["index"]

THEME = "theme"
THEME_STATIC_DIR = "static"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = PAGE_URL + "/index.html"
PAGE_ORDER_BY = "sortorder"


ARTICLE_URL = "notes/{slug}"
ARTICLE_SAVE_AS = ARTICLE_URL + "/index.html"

RELATIVE_URLS = False

CURRENT_YEAR = datetime.datetime.now().year

CSS_FILE = 'main.css'

# Disable unneeded blog functionality.
TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

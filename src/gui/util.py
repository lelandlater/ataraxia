from flask import url_for, session, render_template, current_app
import HTMLParser
# from html.parser import HTMLParser

"""ATARAXIA in Greek."""
hparser=HTMLParser.HTMLParser()
ataraxia='&#x3AC;&#x3C4;&#x3B1;&#x3C1;&#x3B1;&#x3BE;&#x3AF;&#x3B1;'
ataraxia=hparser.unescape(ataraxia)

"""
Generalized navigation. NavBar passed to Jinja, composed of two NavItem lists.
"""
class NavItem(object):

    def __init__(self, url, label):
        self.url = url
        self.label = label

class NavBar(object):

    """
    One list of NavItems, for a centered navigation.
    """
    def __init__(self, start=[], middle=[], end=[]):
        self.start = start
        self.middle = middle
        self.end = end

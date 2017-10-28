from flask import render_template, make_response, url_for
from htmlmin.minify import html_minify
from gui import util

NavBar=util.NavBar
NavItem=util.NavItem

def index():
    nav = NavBar(start=[NavItem('http://google.com', 'API')])
    footer = NavBar(middle=[NavItem(url_for('contact'), 'CONTACT')])
    buttons = [NavItem(url_for('info'), 'INFO'), NavItem(url_for('request_auth'), 'AUTH CODE?')]
    rendered_html = render_template('index.html', nav=nav, buttons=buttons, footer=footer, title='Cue, a social playlist')
    return make_response(html_minify(rendered_html), 200)

def contact():
    items = [NavItem(url_for('index'), 'BACK')]
    rendered_html = render_template('contact.html', items=items, title='Contact Cue')
    return make_response(html_minify(rendered_html), 200)

def info():
    items = [NavItem(url_for('index'), 'BACK')]
    rendered_html = render_template('info.html', items=items, title='More informatioj')
    return make_response(html_minify(rendered_html), 200)

def request_auth():
    items = [NavItem(url_for('index'), 'BACK')]
    rendered_html = render_template('request_auth.html', items=items, title='Authorization')
    return make_response(html_minify(rendered_html), 200)

def access():
    items = [NavItem(url_for('index'), 'BACK')]
    rendered_html = render_template('access.html', items=items, title='Contact Cue')
    return make_response(html_minify(rendered_html), 200)

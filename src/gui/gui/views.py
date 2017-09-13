from flask import render_template, make_response, url_for
from htmlmin.minify import html_minify
from . import util

def index():
    nav = util.NavBar(start=[util.NavItem('http://google.com', 'API')])
    footer = util.NavBar(middle=[util.NavItem(url_for('contact'), 'CONTACT')])
    buttons = []
    rendered_html = render_template('index.html', nav=nav, buttons=buttons, footer=footer, title='Cue: social playlist')
    return make_response(html_minify(rendered_html), 200)

def contact():
    nav = util.NavBar(end=[util.NavItem(url_for('index'), 'BACK')])
    rendered_html = render_template('contact.html', nav=nav, title='Contact Cue')
    return make_response(html_minify(rendered_html), 200)

# -*- coding: utf-8 -*-
#
# Gatling documentation build configuration file

import sys, os

# -- General configuration -----------------------------------------------------

sys.path.append(os.path.abspath('../_sphinx/exts'))
extensions = ['sphinx.ext.todo']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Gatling'
copyright = u'2011-2013, eBusiness Information'
version = '2.0'
release = '2.0'

pygments_style = 'sphinx'
highlight_language = 'scala'
add_function_parentheses = False
show_authors= True

# Show todos while POCing the documentation
todo_include_todos = True

# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'
html_theme_path = ['../_sphinx/themes']
html_favicon = '../_sphinx/static/favicon.ico'
html_title = 'Gatling Documentation'

html_static_path = ['../_sphinx/static']

html_use_smartypants = True
html_domain_indices = False
html_use_index = False
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True

htmlhelp_basename = 'Gatlingdoc'
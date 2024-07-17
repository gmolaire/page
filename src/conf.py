# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Sphinx Markdown Example'
copyright = '2024, Your Name'
author = 'Your Name'
release = '0.1'

# -- General configuration ---------------------------------------------------
extensions = ['recommonmark']

# Setup the parser for markdown files
source_suffix = {
  '.rst': 'restructuredtext',
  '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

import django

project = 'StadtBank'
copyright = '2024, Kafalar Karışık'
author = 'Kafalar Karışık'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib_django',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    "sphinxext.opengraph",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


# https://sphinx-themes.org/
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_theme_options = {
    'repository_url': 'https://github.com/Kafalar-Karisik/StadtBank',
    "repository_branch": "Django-Tailwind",
    'use_repository_button': True,
    'use_issues_button': False,
    'navigation_with_keys': False
}
html_title = "StadtBank"

# The suffix of source filenames.
source_suffix = '.rst'

# -- Open Graph Configuration ------------------------------------------------
# https://sphinxext-opengraph.readthedocs.io/en/latest/

ogp_site_url = "https://kafalar-karisik.github.io/StadtBank/"
ogp_image = "https://opengraph.githubassets.com/6271a1f0466d012fbbf634faea54b21639eff616dbdd86109debc296a45803d8/Kafalar-Karisik/StadtBank"
# ogp_description_length = 300
# ogp_type = "article"
# ogp_custom_meta_tags = [
#    '<meta property="og:ignore_canonical" content="true" />',
# ]
ogp_enable_meta_description = True


# Django Setup
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'StadtBank.settings'
django.setup()

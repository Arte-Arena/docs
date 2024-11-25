import sphinx_rtd_theme

project = 'Space Arena'
copyright = '2024, Leandro Damasio'
author = 'Leandro Damasio'

extensions = [
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'prev_next_buttons_location': 'both',
    'navigation_depth': 4,
}


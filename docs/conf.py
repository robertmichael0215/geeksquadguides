project = 'geek-squad-appointment'
author = 'geek-squad-appointment'
release = '1.0'

# Extensions
extensions = ['sphinx_sitemap']

# Templates
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# JS & Favicon
html_js_files = ['chatbot.js']
html_favicon = '_static/favicon.png'

# Bing verification code
html_context = {
    'bing_verification_code': '739245F5D54BCBF40AC056DC0CBF5710'
}

# Sitemap base URL
html_baseurl = 'https://geeksquadguide.readthedocs.io/en/latest/'

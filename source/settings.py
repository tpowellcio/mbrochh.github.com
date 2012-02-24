THEME = './themes/notmyidea/'
STATIC_PATHS = ['images', ]
TIMEZONE = 'Asia/Singapore'
ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/'
DEFAULT_CATEGORY = 'Blog'

AUTHOR = 'Martin Brochhaus'
SITENAME = 'martinbrochhaus.com'
SITEURL = 'http://www.martinbrochhaus.com'

WITH_PAGINATION = True
DEFAULT_PAGINATION = 10
REVERSE_ARCHIVE_ORDER = True

MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
)

GOOGLE_ANALYTICS = 'UA-1147761-33'
DISQUS_SITENAME = 'martinbrochhauscom'
GITHUB_URL = 'http://github.com/mbrochh/mbrochh.github.com'
TWITTER_USERNAME = 'mbrochh'

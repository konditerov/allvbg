import os

ROOT_PATH = os.path.dirname(__file__)

PROJECT_PATH = '/var/www/pman/data/www/allvbgru'

# Django settings for project.

DEBUG = True
# DEBUG = False
TEMPLATE_DEBUG = DEBUG

USE_I18N = True

ADMINS = (
    ('PMaN', 'pman89@yandex.ru'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'geosite',  # Or path to database file if using sqlite3.
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': '127.0.0.1',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

USE_L10N = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = 'static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    # 'compressor.finders.CompressorFinder',
)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# MEDIA_ROOT = '/var/www/pman/data/www/allvbgru/static/geosite/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
# MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^^dirc^_ctl=7w39yq4+%47$kbn3xth7%$(6b=njd7!cpzluz4'

# TINYMCE_JS_URL = 'http://geosite.ru/static/tiny_mce/tiny_mce_src.js'
# TINYMCE_DEFAULT_CONFIG = {
#     'plugins': "table,spellchecker,paste,searchreplace",
#     'theme': "advanced",
# 	'theme_advanced_toolbar_location' : "top",
# 	'theme_advanced_toolbar_align' : "left",
# 	'theme_advanced_buttons1' : "fullscreen,separator,preview,separator,bold,italic,underline,strikethrough,separator,bullist,numlist,outdent,indent,separator,undo,redo,separator,link,unlink,anchor,separator,image,cleanup,help,separator,code",
# 	'theme_advanced_buttons2' : "",
# 	'theme_advanced_buttons3' : "",
# 	'auto_cleanup_word' : "true",
# 	'plugins' : "table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,searchreplace,print,contextmenu,fullscreen",
# 	'plugin_insertdate_dateFormat' : "%m/%d/%Y",
# 	'plugin_insertdate_timeFormat' : "%H:%M:%S",
# 	'extended_valid_elements' : "a[name|href|target=_blank|title|onclick],img[class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name],hr[class|width|size|noshade],font[face|size|color|style],span[class|align|style]",
# 	'fullscreen_settings' : {
# 		'theme_advanced_path_location' : "top",
# 		'theme_advanced_buttons1' : "fullscreen,separator,preview,separator,cut,copy,paste,separator,undo,redo,separator,search,replace,separator,code,separator,cleanup,separator,bold,italic,underline,strikethrough,separator,forecolor,backcolor,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,help",
# 		'theme_advanced_buttons2' : "removeformat,styleselect,formatselect,fontselect,fontsizeselect,separator,bullist,numlist,outdent,indent,separator,link,unlink,anchor",
# 		'theme_advanced_buttons3' : "sub,sup,separator,image,insertdate,inserttime,separator,tablecontrols,separator,hr,advhr,visualaid,separator,charmap,emotions,iespell,flash,separator,print"
# 	}
# }
# TINYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = False

# STATICFILES_DIRS = (
#	os.path.join(ROOT_PATH, 'static'),
# )

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
    'admin_tools.template_loaders.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'geosite.middleware.UserBasedExceptionMiddleware',
)

INTERNAL_IPS = (
    '127.0.0.1'
)

ROOT_URLCONF = 'urls'

SETTINGS_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_PATH, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATES_PATH = os.path.join(PROJECT_PATH, "templates")

TEMPLATE_DIRS = (
    TEMPLATES_PATH,
)

gettext = lambda s: s
LANGUAGES = (
    ('ru', gettext('Russian')),
    ('en', gettext('English')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

MODELTRANSLATION_TRANSLATION_REGISTRY = 'geosite.translation'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.debug',
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'tinymce',
    'filebrowser',
    'django.contrib.admindocs',
    'easy_thumbnails',
    'mptt',
    'site',
    'feincms',
    'debug_toolbar',
    'modeltranslation',
    'tastypie',
    'compressor',
    'geosite',
)

# DIRECTORY = getattr(SETTINGS, "FILEBROWSER_DIRECTORY", 'uploads/')

YANDEX_MAP_KEY = "AK8Ikk0BAAAAdOLMOgIAjpzOBoj6rXFSZEs52f88oUaPYDAAAAAAAAAAAAB3amaZkCtWNLQzxgaVFWYr-ymltQ==~AFuUaU4BAAAA_nfgKgIA-66Q4jxwCOFrx2v8U1aa6UzHDrYAAAAAAAAAAADAFR7JmJumtVbHoQjeteNT2GZJjA==~AFuUaU4BAAAA_nfgKgIA-66Q4jxwCOFrx2v8U1aa6UzHDrYAAAAAAAAAAADAFR7JmJumtVbHoQjeteNT2GZJjA=="

MPTT_ADMIN_LEVEL_INDENT = 20

AUTH_PROFILE_MODULE = 'geosite.models.UserProfile'

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/www/pman/data/Django_cache',
#         'TIMEOUT': 60,
#         'OPTIONS': {
#             'MAX_ENTRIES': 1000
#         }
#     }
# }

CACHE_MIDDLEWARE_SECONDS = 60

ALLOWED_HOSTS = ['geosite.ru', '*.geosite.ru', 'www.geosite.ru']

# COMPRESS_ENABLED = True
# COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSMinFilter']

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the geosite admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': [],
#             'class': 'django.utils.log.AdminEmailHandler'
#        }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }

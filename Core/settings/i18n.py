import os

DATETIME_FORMAT = os.environ.get('DATETIME_FORMAT', 'H:i, d M Y')

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en')

TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')

USE_I18N = bool(int(os.environ.get('USE_I18N', 1)))

USE_L10N = bool(int(os.environ.get('USE_L10N', 1)))

USE_TZ = bool(int(os.environ.get('USE_TZ', 1)))

LANGUAGES = [(s.strip(), s.strip()) for s in os.environ.get('LANGUAGES', 'en').split(',')]

"""
WSGI config for genqrcode project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import dotenv
from genqrcode.settings import BASE_DIR

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "genqrcode.settings")
dotenv.read_dotenv(os.path.join(BASE_DIR, ".env"),override=True)


application = get_wsgi_application()

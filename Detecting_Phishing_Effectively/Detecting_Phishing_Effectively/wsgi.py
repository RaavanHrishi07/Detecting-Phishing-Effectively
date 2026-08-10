"""
WSGI config for a_robust_approach_for_effective_spam_detection.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Detecting_Phishing_Effectively.settings')
application = get_wsgi_application()

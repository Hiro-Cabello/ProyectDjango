"""
WSGI config for Platzigram project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platzigram.settings')

application = get_wsgi_application()



"""
WSGI  significa web server gateway interface y es un protocolo 
sencillo de llamadas para que un web server (como nginx o apache)
se comuniquen con una aplicacion web o framework escritos 
en python . 

WSGI permite delegar el trabajo de aplicar reglas complejas de enrutamiento
a un web server como NGINIX  y al mismo ...   


"""
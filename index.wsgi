import sae
from blog_project import wsgi

application = sae.create_wsgi_app(wsgi.application)
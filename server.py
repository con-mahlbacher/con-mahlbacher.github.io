from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import os

@view_config(route_name='index', renderer='index.html')
def index(request):
    return {}

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_jinja2_renderer(".html")
        config.add_route('index', '/')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()

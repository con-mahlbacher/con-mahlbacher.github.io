from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.renderers import render
from pyramid.view import view_config
import os

#@view_config(route_name='hello')
def hello_world(request):
    return Response("Hello :(")

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        #config.include('pyramid_jinja2')
        #config.add_jinja2_renderer(".html")
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        #config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
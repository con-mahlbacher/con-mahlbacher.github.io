from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import os

students = [
   {"id": 1, "name": "Ravi", "percent": 75},
   {"id": 2, "name": "Mona", "percent": 80},
   {"id": 3, "name": "Mathews", "percent": 45},
]

@view_config(route_name='index', renderer='templates/myform.html')
def index(request):
    return {}

@view_config(route_name='students', renderer='templates/hello.html')
def add(request):
    student = {'id':request.params['id'],
               'name':request.params['name'],
               'percent':int(request.params['percent'])}
    students.append(student)
    return {'students':students}


if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_jinja2_renderer(".html")
        config.add_route('index', '/')
        config.add_route('students', '/students')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()

# import os
# import settings
# from wsgiref.simple_server import make_server
# from sebkd_framework.main import Sebkdframe
# from urls import urlspatterns
#
# mainapp = Sebkdframe(urlspatterns)
#
# # with make_server(os.environ.get("LOCAL_HOST"), int(os.environ.get("LOCAL_PORT")), mainapp) as httpd:
# with make_server('', 8080, mainapp) as httpd:
#     print(f'Запуск сервера {os.environ.get("LOCAL_HOST")}:{os.environ.get("LOCAL_PORT")}')
#     httpd.serve_forever()
#---------------------------------------------------------
from wsgiref.simple_server import make_server
from sebkd_framework.main import Framework
from urls import routes

# Создаем объект WSGI-приложения
application = Framework(routes)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()
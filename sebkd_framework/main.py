# import os
#
#
# class PageNotFound404:
#     def __call__(self, *args, **kwargs):
#         return os.environ.get('ERROR_404'), os.environ.get('PAGE_NOT_FOUND_404')
#
#
# class Sebkdframe:
#     """wsgi"""
#
#     def __init__(self, routs_obj):
#         self.routs_lst = routs_obj  # при иницилизации получаем список урлов
#
#     def __call__(self, _environ, _start_response):
#         # Получаем адрес, по которому пользователь выполнил переход
#         path = _environ['PATH_INFO']
#
#         if not path.endswith('/'):
#             path = f'{path}/'
#
#             # определяем есть ли у нас контроллер для отработки страницы
#             if path in self.routs_lst:
#                 view = self.routs_lst[path]
#             else:
#                 view = PageNotFound404()
#
#             # Запускаем контроллер
#             code, body = view()
#             _start_response(code, [('Content-Type', 'text/html')])
#             return [body.encode('utf-8')]
#---------------------------------------------------------------------
class PageNotFound404:
    def __call__(self):
        return '404 WHAT', '404 PAGE Not Found'


class Framework:

    """Класс Framework - основа WSGI-фреймворка"""

    def __init__(self, routes_obj):
        self.routes_lst = routes_obj

    def __call__(self, environ, start_response):
        # Получаем адрес, по которому пользователь выполнил переход
        path = environ['PATH_INFO']

        # Добавляем закрывающий слеш
        if not path.endswith('/'):
            path = f'{path}/'

        # Находим нужный контроллер
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()

        # Запускаем контроллер
        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
import os

class PageNotFound404:
    def __call__(self, *args, **kwargs):
        return os.environ['ERROR_404'], os.environ['PAGE_NOT_FOUND_404']


class Sebkdframe:
    """wsgi"""

    def __init__(self, routes_obj):
        self.routes_lst = routes_obj  # при иницилизации получаем список урлов

    def __call__(self, environ, start_response):
        # Получаем адрес, по которому пользователь выполнил переход
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        # определяем есть ли у нас контроллер для отработки страницы
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()

        # Запускаем контроллер
        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
#---------------------------------------------------------------------
